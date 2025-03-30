from hashid import HashID
import subprocess

def cracker():
    ascii_art = r"""

██╗    ██╗██╗  ██╗ █████╗ ████████╗    ████████╗██╗  ██╗███████╗    ██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██████╗ 
██║    ██║██║  ██║██╔══██╗╚══██╔══╝    ╚══██╔══╝██║  ██║██╔════╝    ██║  ██║██╔══██╗██╔════╝██║  ██║    ╚════██╗
██║ █╗ ██║███████║███████║   ██║          ██║   ███████║█████╗      ███████║███████║███████╗███████║      ▄███╔╝
██║███╗██║██╔══██║██╔══██║   ██║          ██║   ██╔══██║██╔══╝      ██╔══██║██╔══██║╚════██║██╔══██║      ▀▀══╝ 
╚███╔███╔╝██║  ██║██║  ██║   ██║          ██║   ██║  ██║███████╗    ██║  ██║██║  ██║███████║██║  ██║      ██╗   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═╝   
                                                                                                                


    """
    print(ascii_art)




    user_hash = input("Enter the hash: ").strip()
    hid = HashID()
    results = list(hid.identifyHash(user_hash))

    if results:
        print("Possible hash types:")
        print("hash", "|||", "mode number")

        for i in results[:5]:
            hash_name = i[0]
            mode = i[1]  # this is the hashcat mode number

            print("", hash_name, "|||", mode if mode else "N/A")

            if mode is not None:
                subprocess.run([
                    "hashcat",
                    "-m", str(mode),
                    "--potfile-disable",
                    "--quiet",
                    "--force",
                    user_hash,
                    "/usr/share/wordlists/rockyou.txt"
                ])
    else:
        print("kuch nhi mila")

cracker()
