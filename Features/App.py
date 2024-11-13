from speak import speak
from takecommand import takeCommand
import os

if __name__ == "__main__":
    speak()
    while True:
        query = takeCommand().lower()   

        if "open vs code" in query:
            # Change path as per your application directory
            Path = "C:\\Users\\mdjun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)

        elif "open whatsapp" in query:
            # Get-AppxPackage *WhatsApp* run in powershell to get application location
            Path = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2444.5.0_x64__cv1g1gvanyjgm\\WhatsApp"
            os.startfile(Path)

        elif "open canva" in query:
            Path = "C:\\Users\\mdjun\\AppData\\Local\\Programs\\Canva\\Canva.exe"
            os.startfile(Path)

        elif "open telegram" in query:
            Path = "C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_5.5.5.0_x64__t4vj0pshhgkwm\\Telegram"
            os.startfile(Path)

        elif "open camera" in query:
            Path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2024.2408.1.0_x64__8wekyb3d8bbwe\\WindowsCamera"
            os.startfile(Path)

        elif "open word" in query:
            Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
            os.startfile(Path)

        elif "open excel" in query:
            Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
            os.startfile(Path)

        elif "open powerpoint" in query:
            Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
            os.startfile(Path)

        