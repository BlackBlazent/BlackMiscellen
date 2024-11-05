from spotifyDownloader import ( handle_download, download_spotify_playlist, download_spotify_audio, download_spotify_podcast)

def spotify_menu():
    """Main menu for Spotify download options."""
    while True:
        print("\nSpotify Download Options:")
        print("1. Download Spotify Playlist")
        print("2. Download Spotify Audio")
        print("3. Download Spotify Podcast")
        print("4. Back to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            url = input("Enter the Spotify playlist link: ")
            handle_download(url, download_spotify_playlist)
        elif choice == '2':
            url = input("Enter the Spotify audio link: ")
            handle_download(url, download_spotify_audio)
        elif choice == '3':
            url = input("Enter the Spotify podcast link: ")
            handle_download(url, download_spotify_podcast)
        elif choice == '4':
            break
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    spotify_menu()
