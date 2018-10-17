import os,sys
def createDir(dirName):
    try:
        os.mkdir(dirName)
    except:
        print("Directory "+dirName+" already exists")


def toolInstallation(toolName):
     createDir(toolName+"/Installation")
     with open("txt/$TOOL+INSTALLATION.txt", "rt") as txtInstallation:
        with open(toolName+"/Installation/"+toolName+'Tool.java', "wt") as javaInstallation:
            for line in txtInstallation:
                if '$TOOL+NAME' in line:
                    javaInstallation.write(line.replace('$TOOL+NAME', toolName))
                else:
                    javaInstallation.write(line.replace('$TOOL+INSTALLATION',toolName+'Tool'))     


def tooInstaller(toolName):
    createDir(toolName+"/Installation")
    with open("txt/$TOOL+INSTALLER.txt", "rt") as txtInstaller:
        with open(toolName+"/Installation/"+toolName+'Installer.java', "wt") as javaInstaller:
            for line in txtInstaller:
                javaInstaller.write(line.replace('$TOOL+INSTALLER', toolName+'Installer'))
            
                
def toolUtil(toolName):
    createDir(toolName+"/util")
    with open("txt/$TOOL+UTIL.txt", "rt") as txtUtil:
        with open(toolName+"/util/"+toolName+'Util.java', "wt") as javaUtil:
            for line in txtUtil:
                javaUtil.write(line.replace('$TOOL+UTIL', toolName+'Util'))


def toolBuilder(toolName):
    with open("txt/$TOOL+BUILDER.txt", "rt") as txtBuilder:
        with open(toolName+"/"+toolName+'Builder.java', "wt") as javaBuilder:
            for line in txtBuilder:
                if "$TOOL+UTIL" in line:
                    javaBuilder.write(line.replace('$TOOL+UTIL', toolName+'Util')) 
                else:    
                    javaBuilder.write(line.replace('$TOOL+BUILDER', toolName+'Builder'))


def toolWrapper(toolName):
    with open("txt/$TOOL+WRAPPER.txt", "rt") as txtWrapper:
        with open(toolName+"/"+toolName+'Wrapper.java', "wt") as javaWrapper:
            for line in txtWrapper:
                if "$TOOL+INSTALLATION" in line:
                    javaWrapper.write(line.replace('$TOOL+INSTALLATION',toolName+'Tool'))
                elif "$TOOL+UTIL" in line:
                    javaWrapper.write(line.replace('$TOOL+UTIL', toolName+'Util'))
                else:
                    javaWrapper.write(line.replace('$TOOL+WRAPPER', toolName+'Wrapper')) 


def toolPublisher(toolName):
    with open("txt/$TOOL+PUBLISHER.txt", "rt") as txtPublisher:
        with open(toolName+"/"+toolName+'Publisher.java', "wt") as javaPublisher:
            for line in txtPublisher:
                javaPublisher.write(line.replace('$TOOL+PUBLISHER', toolName+'Publisher'))            

def main():
    
    if len(sys.argv) != 2:
        exit("Usage: python jenkinsPluginGen.py (--The Tool's Name--)")
    
    pluginName = sys.argv[1]
    isValid = False
    
    try:
        int(pluginName)
    except ValueError:
        isValid = True

    if isValid:
        createDir(pluginName) 
    else:
        exit("Need to enter a vaild name - exiting now")

    selected = raw_input("Generate: \n[1] Tool Simple Installer\n[2] Tool Installation\n[3] Simple Wrapper\n[4] Build Step\n[5] Post-Build Action\n[6] Utility\n[7] All\n[8] Exit\n")


    if selected == '1':
        tooInstaller(pluginName)
    elif selected == '2':
        toolInstallation(pluginName)
    elif selected == '3':
        toolWrapper(pluginName)
    elif selected == '4':
        toolBuilder(pluginName)
    elif selected == '5':
        toolPublisher(pluginName)
    elif selected == '6':
        toolUtil(pluginName)
    elif selected == '7':
        tooInstaller(pluginName)
        toolInstallation(pluginName)
        toolWrapper(pluginName)
        toolBuilder(pluginName)
        toolPublisher(pluginName)
        toolUtil(pluginName)
    elif selected == '8':
        if len(os.listdir(pluginName)) == 0:
            os.rmdir(pluginName)
        exit("Bye :)")
    else:
        exit("Not in the range 1-7 - exiting now")

if __name__ == "__main__":
    main()