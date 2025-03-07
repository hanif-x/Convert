import os
import re
import sys

# 🔥 Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# 🔥 Banner
def show_banner():
    print(f"""{BLUE}
    ╔═══════════════════════════════════════════╗
    ║         CODE CONVERTER TOOL               ║
    ║   Convert Between Python, Java, C++, JS   ║
    ║       {YELLOW}By Hanif{BLUE}                           ║
    ╚═══════════════════════════════════════════╝
    {RESET}""")

# 🔥 Function to Convert Code
def convert_code(file_path, from_lang, to_lang):
    with open(file_path, "r") as f:
        code = f.read()

    converted_code = None
    new_ext = None

    if from_lang == "python" and to_lang == "java":
        # Python → Java
        code = code.replace("def ", "public static void ")
        code = re.sub(r"print(.*?)", r"System.out.println(\1);", code)
        code = code.replace(":", " {")
        code = code.replace("\n", " }\n")

        converted_code = "public class ConvertedCode {\n    public static void main(String[] args) {\n" + code + "\n    }\n}"
        new_ext = "java"

    elif from_lang == "java" and to_lang == "python":
        # Java → Python
        code = code.replace("public static void ", "def ")
        code = re.sub(r"System.out.println(.*?);", r"print(\1)", code)
        code = code.replace(" {", ":")
        code = code.replace(" }", "")

        converted_code = code
        new_ext = "py"

    elif from_lang == "python" and to_lang == "cpp":
        # Python → C++
        code = code.replace("def ", "void ")
        code = re.sub(r"print(.*?)", r'std::cout << \1 << std::endl;', code)
        code = code.replace(":", " {")
        code = code.replace("\n", " }\n")

        converted_code = "#include <iostream>\nusing namespace std;\n\n" + "int main() {\n" + code + "\n    return 0;\n}"
        new_ext = "cpp"

    elif from_lang == "cpp" and to_lang == "python":
        # C++ → Python
        code = code.replace("int main()", "def main():")
        code = re.sub(r"std::cout << (.*?);", r"print(\1)", code)
        code = code.replace("{", ":")
        code = code.replace("}", "")

        converted_code = code
        new_ext = "py"

    elif from_lang == "python" and to_lang == "js":
        # Python → JavaScript
        code = code.replace("def ", "function ")
        code = re.sub(r"print(.*?)", r"console.log(\1);", code)
        code = code.replace(":", " {")
        code = code.replace("\n", " }\n")

        converted_code = code
        new_ext = "js"

    elif from_lang == "js" and to_lang == "python":
        # JavaScript → Python
        code = code.replace("function ", "def ")
        code = re.sub(r"console.log(.*?);", r"print(\1)", code)
        code = code.replace(" {", ":")
        code = code.replace(" }", "")

        converted_code = code
        new_ext = "py"

    else:
        return None, None

    return converted_code, new_ext

# 🔥 User Interaction Function
def main():
    show_banner()

    file_path = input(f"{YELLOW}🔹 Enter file name (Example: test.py): {RESET}").strip()

    if not os.path.exists(file_path):
        print(f"{RED}🚫 File not found!{RESET}")
        return

    ext = file_path.split('.')[-1]
    lang_map = {
        "py": "python",
        "java": "java",
        "cpp": "cpp",
        "js": "js"
    }

    from_lang = lang_map.get(ext, None)

    if not from_lang:
        print(f"{RED}🚫 Unsupported file format!{RESET}")
        return

    # 🔥 User Selects Conversion Language
    print(f"{GREEN}\n🔄 Convert {from_lang.capitalize()} to:{RESET}")
    print("1️⃣ Java")
    print("2️⃣ C++")
    print("3️⃣ JavaScript")
    print("4️⃣ Python")
    
    choice = input(f"{YELLOW}🔸 Your choice (1-4): {RESET}").strip()

    lang_options = {
        "1": "java",
        "2": "cpp",
        "3": "js",
        "4": "python"
    }

    to_lang = lang_options.get(choice, None)

    if not to_lang or to_lang == from_lang:
        print(f"{RED}🚫 Invalid choice!{RESET}")
        return

    # 🔥 User Selects Save Location
    print(f"{GREEN}\n📂 Where do you want to save the converted file?{RESET}")
    print("1️⃣ Default (downloads folder)")
    print("2️⃣ Custom location")

    save_choice = input(f"{YELLOW}🔸 Your choice (1 or 2): {RESET}").strip()

    if save_choice == "2":
        save_folder = input(f"{YELLOW}📁 Enter custom folder path: {RESET}").strip()
    else:
        save_folder = "downloads"

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # 🔥 Convert & Save
    converted_code, new_ext = convert_code(file_path, from_lang, to_lang)

    if converted_code:
        new_file_name = os.path.splitext(os.path.basename(file_path))[0] + f"_converted.{new_ext}"
        new_file_path = os.path.join(save_folder, new_file_name)

        with open(new_file_path, "w") as f:
            f.write(converted_code)

        print(f"\n✅ {GREEN}Successfully converted!{RESET}")
        print(f"📁 New file saved at: {BLUE}{new_file_path}{RESET}\n")
    else:
        print(f"{RED}❌ Conversion failed!{RESET}")

if __name__ == "__main__":
    main()
