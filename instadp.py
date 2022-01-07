import instaloader

loader = instaloader.Instaloader()
username = input("Enter username: ")
loader.download_profile(username,profile_pic_only=True)
input("Enter to close")
