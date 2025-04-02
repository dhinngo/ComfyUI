from pathlib import Path

# gitignore の対象パス
base_gitignore = [
    "__pycache__/",
    "*.py[cod]",
    "/output/",
    "/input/",
    "!/input/example.png",
    "/models/",
    "/temp/",
    "/custom_nodes/",
    "!custom_nodes/example_node.py.example",
    "extra_model_paths.yaml",
    "/.vs",
    ".vscode/",
    ".idea/",
    "venv/",
    ".venv/",
    "/web/extensions/*",
    "!/web/extensions/logging.js.example",
    "!/web/extensions/core/",
    "/tests-ui/data/object_info.json",
    "/user/",
    "*.log",
    "web_custom_versions/",
    ".DS_Store"
]

# 追跡したい重要パス（除外解除したいやつ）
keep_paths = [
    "!models/checkpoints/**",
    "!models/clip/**",
    "!models/diffusion_models/**",
    "!models/loras/**",
    "!models/vae/**",
    "!models/configs/**",
    "!custom_nodes/**",
    "!user/default/workflows/**"
]

# ファイルの書き込み先
gitignore_path = Path(".gitignore")

# 書き込み処理
with gitignore_path.open("w", encoding="utf-8") as f:
    for line in base_gitignore:
        f.write(line.strip() + "\n")
    f.write("\n# === 以下は追跡したい重要フォルダ ===\n")
    for line in keep_paths:
        f.write(line.strip() + "\n")

print("✅ .gitignore を更新しました！")
