## gen_menu_sfx.py - 生成主界面按钮的悬停 / 点击音效（纯标准库，无需任何依赖）
##
## 设计取向：纸页与木质感的极短"嗒"声，不用合成器味很重的电子哔声。
##   hover  —— 40ms，高频轻微摩擦音，像指尖扫过纸面/木牌边缘，很轻（peak 0.22）
##   click  —— 80ms，低频木质感"咚"加一点点纸声，确认感明确（peak 0.5）
##
## 用法：python gen_menu_sfx.py <输出目录>

import math
import os
import random
import struct
import sys
import wave

SR = 44100


def env(n, attack, decay):
    """起音 + 指数衰减包络。"""
    out = []
    a = max(1, int(attack * SR))
    for i in range(n):
        if i < a:
            e = i / a
        else:
            e = math.exp(-(i - a) / (decay * SR))
        out.append(e)
    return out


def fade_tail(samples, ms=6):
    k = max(1, int(SR * ms / 1000.0))
    n = len(samples)
    for i in range(min(k, n)):
        samples[n - 1 - i] *= (i / k)
    return samples


def damped(n, freq, decay, amp=1.0, phase=0.0):
    out = [0.0] * n
    for i in range(n):
        t = i / SR
        out[i] = amp * math.exp(-t / decay) * math.sin(2 * math.pi * freq * t + phase)
    return out


def noise_burst(n, decay, amp=1.0, lp=0.35, rng=None):
    """低通过的噪声：lp 越小越闷。"""
    out = [0.0] * n
    prev = 0.0
    for i in range(n):
        t = i / SR
        prev = prev + lp * ((rng.uniform(-1.0, 1.0)) - prev)
        out[i] = amp * math.exp(-t / decay) * prev
    return out


def mix(*layers):
    n = max(len(x) for x in layers)
    out = [0.0] * n
    for layer in layers:
        for i, v in enumerate(layer):
            out[i] += v
    return out


def normalize(samples, peak):
    m = max(abs(v) for v in samples) or 1.0
    return [v * (peak / m) for v in samples]


def write_wav(path, samples):
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        frames = b"".join(
            struct.pack("<h", int(max(-1.0, min(1.0, v)) * 32767)) for v in samples
        )
        w.writeframes(frames)


def make_hover():
    rng = random.Random(20261022)
    n = int(0.040 * SR)

    body = mix(
        [a * b for a, b in zip(damped(n, 1750, 0.010, 1.0), env(n, 0.002, 0.012))],
        [a * b for a, b in zip(damped(n, 2680, 0.006, 0.45), env(n, 0.001, 0.008))],
        [a * b for a, b in zip(noise_burst(n, 0.006, 0.35, 0.55, rng), env(n, 0.001, 0.010))],
    )

    body = fade_tail(normalize(body, 0.22), 4)
    return body


def make_click():
    """按钮点击：一声短促的"咔"。

    不是"嘀"（纯高频正弦会变成电子提示音），也不是"咚"（太低会闷）。
    做法：2.2kHz + 1.4kHz 的木质瞬态打底，700Hz 给一点"厚度"，
    再加一小撮经过低通的噪声当摩擦边缘，整体 65ms 收干净。
    """

    rng = random.Random(20261026)
    n = int(0.065 * SR)

    body = mix(
        ## 主瞬态：2.2kHz，"咔"的芯（比纯高频柔和，不会像嘀）
        [a * b for a, b in zip(damped(n, 2200, 0.009, 1.0), env(n, 0.0006, 0.016))],
        ## 次瞬态：1.4kHz，带一点尾巴，塑料/木头质感
        [a * b for a, b in zip(damped(n, 1400, 0.014, 0.55), env(n, 0.0008, 0.024))],
        ## 厚度：700Hz 短促下沉，去掉"嘀"的尖锐感
        [a * b for a, b in zip(damped(n, 700, 0.018, 0.40), env(n, 0.0010, 0.030))],
        ## 摩擦边缘：低通过的噪声，只留一点点高频
        [a * b for a, b in zip(noise_burst(n, 0.0050, 0.55, 0.55, rng), env(n, 0.0003, 0.010))],
    )

    body = fade_tail(normalize(body, 0.52), 5)
    return body


def make_swoosh(rising):
    """界面唤醒 / 退出音效：一声"刷"，音高由低到高（唤醒）或由高到低（退出）。

    做法：白噪声过一个截止频率随时间扫动的带通（Chamberlin 状态变量滤波器），
    再叠一点同频的正弦当"气声的芯"，包络做成快起、慢收的刷子感。
    """

    rng = random.Random(20261024 if rising else 20261025)

    dur = 0.32 if rising else 0.28
    n = int(dur * SR)

    f_start = 360.0 if rising else 3100.0
    f_end = 3100.0 if rising else 360.0
    peak_pos = 0.58 if rising else 0.24

    env_curve = []

    pk = max(1, int(peak_pos * n))
    for i in range(n):
        if i < pk:
            env_curve.append((i / pk) ** 1.3)
        else:
            env_curve.append(((n - i) / (n - pk)) ** 1.7)

    low = 0.0
    band = 0.0
    damp = 0.55
    out = []

    for i in range(n):

        u = i / float(n)
        fc = f_start * ((f_end / f_start) ** u)

        f = 2.0 * math.sin(math.pi * fc / SR)
        if f > 1.4:
            f = 1.4

        x = rng.uniform(-1.0, 1.0)
        low += f * band
        high = x - low - damp * band
        band += f * high

        # 带通 + 一点低通当厚度，再叠 12% 的同频正弦
        tone = math.sin(2 * math.pi * fc * 1.5 * (i / SR))

        out.append((band * 1.0 + tone * 0.12) * env_curve[i])

    body = fade_tail(normalize(out, 0.42), 8)
    return fade_head(body, 4)


def make_woodblock():
    """界面唤出音效：像敲木鱼的一记较清脆的"咚"。

    木鱼的特征是"腔体共鸣"：几个不成整数倍的共振峰 + 极短的起音 + 干净的衰减，
    没有噪声尾巴（噪声一多就变成"刷"或"嗒"）。这里用
      380Hz（腔体底子）+ 780Hz（主音）+ 1170Hz（次泛音）+ 1980Hz（敲击的脆感）
    四层指数衰减，再加 1.2ms 的高频瞬态表示"敲"的那一下。
    """

    rng = random.Random(20261028)
    n = int(0.26 * SR)

    body = mix(
        ## 腔体底子：380Hz，衰减慢一点，给出"咚"的厚度
        [a * b for a, b in zip(damped(n, 380, 0.085, 0.55), env(n, 0.0015, 0.20))],
        ## 主音：780Hz，木鱼最响的那一口
        [a * b for a, b in zip(damped(n, 780, 0.055, 1.00), env(n, 0.0010, 0.13))],
        ## 次泛音：1170Hz，让音色不闷
        [a * b for a, b in zip(damped(n, 1170, 0.032, 0.42), env(n, 0.0008, 0.075))],
        ## 脆感：1980Hz，只留很短一瞬
        [a * b for a, b in zip(damped(n, 1980, 0.014, 0.20), env(n, 0.0006, 0.030))],
        ## 敲击瞬态：极短的高通噪声，起音的"木"感
        [a * b for a, b in zip(noise_burst(n, 0.0028, 0.30, 0.75, rng), env(n, 0.0003, 0.006))],
    )

    body = fade_tail(normalize(body, 0.62), 12)
    return fade_head(body, 1)


def fade_head(samples, ms=4):
    k = max(1, int(SR * ms / 1000.0))
    n = len(samples)
    for i in range(min(k, n)):
        samples[i] *= (i / k)
    return samples


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out_dir, exist_ok=True)

    jobs = (
        ("ui_hover.wav", make_hover),
        ("ui_click.wav", make_click),
        ("ui_menu_in.wav", make_woodblock),
        ("ui_menu_out.wav", lambda: make_swoosh(False)),
        )

    for name, fn in jobs:
        samples = fn()
        path = os.path.join(out_dir, name)
        write_wav(path, samples)
        peak = max(abs(v) for v in samples)
        print("%s  %d frames  %.3fs  peak=%.3f" % (name, len(samples), len(samples) / SR, peak))


if __name__ == "__main__":
    main()
