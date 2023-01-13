```
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄    ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
█       █       █       █      █  █      ██       █       █   ▄  █ █  █ █  █       █       █
█   ▄   █  ▄▄▄▄▄█▄     ▄█  ▄   █  █  ▄    █    ▄▄▄█       █  █ █ █ █  █▄█  █    ▄  █▄     ▄█
█  █▄█  █ █▄▄▄▄▄  █   █ █ █▄█  █  █ █ █   █   █▄▄▄█     ▄▄█   █▄▄█▄█       █   █▄█ █ █   █  
█       █▄▄▄▄▄  █ █   █ █      █  █ █▄█   █    ▄▄▄█    █  █    ▄▄  █▄     ▄█    ▄▄▄█ █   █  
█   ▄   █▄▄▄▄▄█ █ █   █ █  ▄   █  █       █   █▄▄▄█    █▄▄█   █  █ █ █   █ █   █     █   █  
█▄▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄█ █▄▄█  █▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█ █▄▄▄█ █▄▄▄█     █▄▄▄█  
```

created by [dodo_sec](https://twitter.com/dodo_sec)

# asta-decrypt
This is a simple script that implements the decryption routine for the encrypted final stage used by the Astaroth/Guildma malware family.

Astaroth uses an AutoIT script with an embedded DLL that writes the final payload to disk as `db.temp` and injects it into a hollow process.

This script will turn that file into its decrypted form, which will be named **asta-decrypted.exe**.

Unfortunately, **for the encrypted file to be written to disk you'll need to run the AutoIT script successfully.**

Either place `asta-decrypt.py` in the same directory as `db.temp` or edit the code to match the path of the input file.
