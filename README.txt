Note: This set of instructions is really brief, there should be pictures and screenshots added to make it more usable, but I hope this is enough to get you running.

Equipment required
  - laptop with a SDCard slot.
  - DragonBoard and power supply
  - Monitor with HDMI input (or a large screen TV)
  - USB dongle, keyboard/trackpad unit (or a USB Keyboard and USB mouse)
  - A USB memory stick, 256MB is lots.
  - 8GB SDCard  for installing Debian on the DragonBoard 410c
    - You cannot (easily) reuse the SDCard that you put the Debian installer on, it is formatted strangely.
 
Debian Install Procedure (this will fail if a Linker card or a Sensor card is attached to the DragonBoard 410c, remove any Mezzanine board before attempting to install the OS).
  - On your Laptop, open the 96Boards software directory https://builds.96boards.org/snapshots/dragonboard410c/linaro/debian/84/ 
    - Note: I used 84, but newer builds should work. Change the 84 to ‘latest’.
  - Download the Debian SDCard install file "dragonboard410c_sdcard_install_debian-84.zip" to your local Downloads directory. This is the only file you need from the directory.
  - Right click on the downloaded zip file and select "extract All.." remember where you extracted to!
  - Copy the two files "breakerball.tar" and "Install" to your Downloads directory from HERE.
  - Put the USB stick into a USB port on your laptop. Ensure it has at least 256MB of free space.
  - Right click on the USB Stick and format it, ensure the disk name is "DRAGON", this name is used later.
  - Copy the files from your Download directory to the USB Stick.
    - You should have 2 files, "Install" and "breakerball.tar".
  - Remove the USB Stick from your laptop and set it aside for now.
  - Start WinDisk32Imager.exe, (if you do not have this program download and install it from https://sourceforge.net/projects/win32diskimager/ )
  - Put the Install SDCard into the SDCard slot on your laptop.
  - Use Win32DiskImager to copy the file you extracted from the 96Boards download in the steps above. The extracted file “db410_sd_install_debian.img” is copied to the Install SDCard.
    - Select the img file, then press the "Write" button to copy it over (about 5 minutes)
  - Remove the Install SDCard from the laptop and insert it into the DragonBoard
  - On the DragonBoard 410c ensure DIP switch 2 (SD Boot) is turned ON, all others off
  - Connect the USB Keyboard/Mouse to the DragonBoard
  - Connect the HDMI monitor to the DragonBoard
  - Connect the power supply. The Board should display the installer in about 15 seconds
  - Run the Install by hitting the ‘i’ then <Enter> keys (about 2 minutes 20 seconds)
  - Remove power from the board
 
Now that Debian is installed we can connect the Linker or Sensors card to the 410c.
  - Remove the Install SDCard, and connect the USB Stick to a USB port
  - Connect the Linker card, or the Sensors card to the DragonBoard410c.
    - Take the time to install all of the standoffs and screws.
    - Be REALLY careful that you have the connector correctly aligned, if you have the connector in the wrong place it is fatal to one or both of the boards!
  - Attach the peripherals to the mezzanine board.
    - The Linker Board needs a white cable from ADC1 to the slide pot.
    - The Sensors board needs two multi-colour cables
      - One from A1 to the rotary pot
      - One from I2C0 to the 2x16 LCD display.
  - Connect power to the DragonBoard, it should boot to Debian in about 20 seconds.
  - Click on the network icon in the lower right of the screen and WiFi connect to Hydra (or any other network). 
    - You need this because the install script loads a bunch of stuff from the net.
  - Open a command window: click Debian Start -> System Tools -> LXTerminal
  - In the LXTerminal Window enter the following commands
    - cp /media/linaro/DRAGON/*  .
    - chmod +x Install
    - ./Install
  - The Install script will extract the zip files, put icons on the desktop, install code onto the Sensors mezzanine board (if connected) and (if necessary) update the operating system. (about 10 minutes)
  - Once the script completes you should see one of two BreakerBall icons, one for the Sensors board, or one for the Linker Board
  - Double Click on the BreakerBall icon.
    - It will ask you if you want to Execute, or Execute in a terminal, doesn’t matter which you choose.
    - When scratch starts click OK to acknowledge that remote sensors are running, 
    - click on the green flag in the upper right corner of the scratch window to start the game
    - click on the full-screen icon in the upper right corner of the scratch window
    - you have 15 seconds to perform the above three steps.
  - After 15 seconds the program to read the slider or pot will start and transmit the paddle position to scratch.
  - Play the game (it cheats).


