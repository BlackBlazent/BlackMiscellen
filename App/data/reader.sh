#!/bin/bash
# reader.sh

# Define the list of files and directories to verify
FILES=(
    "./App/app.py"
    "./App/manifest/manifest"
    "./App/data/reader.sh"
    "./App/data/package.json"
    "./App/data/api/spotifyAPI.db"
    "./App/data/api/spotifyAPI.json"
    "./App/data/auth/facebook/facebook.details.json"
    "./App/data/auth/instaloader/instagram.details.json"
    "./App/data/auth/instaloader/session-your_username"
    "./App/data/forbidden/Khah.Jvssljavy.py"
    "./App/data/forbidden/blackmiscellen.db"
    "./App/data/forbidden/backup_gathering.sh"
    "./App/data/forbidden/backup.py"
    "./App/data/locales/arabic.py"
    "./App/data/locales/french.py"
    "./App/data/locales/german.py"
    "./App/data/locales/japanese.py"
    "./App/data/locales/korean.py"
    "./App/data/locales/mandarin_chinese.py"
    "./App/data/locales/portogues.py"
    "./App/data/locales/russian.py"
    "./App/data/locales/spanish.py"
    "./App/data/locales/thailand.py"
    "./App/home/user/installed/"
    "./App/home/user/miscellen/"
    "./App/lib/ffmpeg/ffmpeg.linux.py"
    "./App/lib/ffmpeg/ffmpeg.macos.py"
    "./App/lib/ffmpeg/ffmpeg.windows.py"
    "./App/lib/python/python.linux.py"
    "./App/lib/python/python.macos.py"
    "./App/lib/python/python.windows.py"
    "./App/embedded/ffmpeg/Linux/"
    "./App/embedded/ffmpeg/MacOs/"
    "./App/embedded/ffmpeg/Windows/"
    "./App/embedded/python/Linux/"
    "./App/embedded/python/MacOs/"
    "./App/embedded/python/Windows/"
    "./docs/miscellen.png"
    "./graph/graph.md"
    "./License/License"
    "./modules/SocMEd/Facebook.py"
    "./modules/SocMEd/YouTube.py"
    "./modules/SocMEd/Snapchat.py"
    "./modules/SocMEd/TikTok.py"
    "./modules/SocMEd/Pinterest.py"
    "./modules/SocMEd/Threads.py"
    "./modules/SocMEd/Spotify.py"
    "./modules/SocMEd/Twitter.py"
    "./modules/SocMEd/Instagram.py"
    "./modules/torrent/torrent.py"
    "./Out/Facebook/"
    "./Out/YouTube/"
    "./Out/Instagram/"
    "./Out/Threads/"
    "./Out/Twitter/"
    "./Out/Snapchat/"
    "./Out/TikTok/"
    "./Out/Pinterest/"
    "./Out/Spotify/"
    "./src/banners/banner.py"
    "./src/banners/bannerList/"
    "./src/book/bible.py"
    "./src/book/book-chapter/"
    "./src/icon/miscellen.png"
    "./temp/temp.log.txt"
    "./ui/ui.py"
    "./ui/index.html"
    "./BlackMiscellen.py"
    "./checklist.yml"
    "./cookies.txt"
    "./docker-compose.yml"
    "./Dockerfile"
    "./embed.installer.py"
    "./miscellen-ui.x0.9.py"
    "./pyproject.toml"
    "./README.md"
    "./requirements.tx"
    "./restore.py"
    "./setup"
    "./setup.py"
    "./update.py"
)

# Check each file and directory
missing_files=()
for file in "${FILES[@]}"; do
    if [[ ! -e "$file" ]]; then
        missing_files+=("$file")
    fi
done

# Output results
if [[ ${#missing_files[@]} -eq 0 ]]; then
    echo "All required files and directories are present."
else
    echo "The following files or directories are missing:"
    for missing in "${missing_files[@]}"; do
        echo "$missing"
    done
fi
