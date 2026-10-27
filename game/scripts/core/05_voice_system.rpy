## 05_voice_system.rpy - 角色配音管理系统与台账支持
## 支持结构化配音元数据、自动寻址与无障碍语音提示

init -1 python:
    import json, os

    class VoiceLineManager:
        def __init__(self):
            self.registry = {}
            self.load_manifest()

        def load_manifest(self):
            manifest_path = os.path.join(config.gamedir, "scripts", "core", "voice_manifest.json")
            if os.path.exists(manifest_path):
                try:
                    with open(manifest_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        for item in data:
                            self.registry[item["id"]] = item
                except Exception as e:
                    print("Voice manifest load failed:", e)

        def get_file(self, line_id):
            if line_id in self.registry:
                return f"audio/voice/{self.registry[line_id]['file']}"
            return f"audio/voice/{line_id}.ogg"

        def get_info(self, line_id):
            return self.registry.get(line_id, None)

    voice_mgr = VoiceLineManager()
