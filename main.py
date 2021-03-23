import speech_recognition as sr
import sys
import subprocess
import time
import os
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    #r.energy_threshold = 1500
    def Capture_speech():
        print('Speak anything: ')
        audio = r.record(source, duration=4)

        try:
            finish_var = 0
            text = r.recognize_google(audio)
            command = None
            command = format(text)
            print("**************************")
            print('COMMAND: {}'.format(text))
            print("**************************")

            if 'Jarvis' in command:
                print("------------------------")
                print('WELCOME SIR!')
                print("------------------------")

            if 'help' in command:
                print("--------------------HELP-1---------------------")
                print('To search Google with Firefox, say:')
                print('search Firefox [input]')
                print('(be advised, in this version, only the first word after Firefox will be used as input)')
                print("--------------------HELP-2----------------------")
                print('To close / quit the program, say:')
                print('finish')
                print("--------------------HELP-3----------------------")
                print('To search for a file in your directory, say:')
                print('search directory for [input]')
                print('(be advised, in this version, only the files starting with the input will be found)')
                print("--------------------HELP-4---------------------")
                print("Press ENTER to close the HELP section.")
                print("------------------------------------------------")
                input("")

            if 'open' in command and 'firefox' in command:
                print("------------------------")
                print('Opening firefox.exe!')
                print("------------------------")
                subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])

            if 'search' in command and 'Firefox' in command:
                search_firefox = command.split()[2]
                print("------------------------")
                print('Searching for: ', search_firefox)
                print("------------------------")
                url = 'https://www.google.at/search?q='
                url_firefox = url + search_firefox
                print("Firefox search query:")
                print(url_firefox)
                print("------------------------")
                firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
                webbrowser.get(firefox_path).open(url_firefox)

            if  'finish' in command: 
                print("----------------------------------------")
                print('FBI and CIA have stopped listening ...')
                print("----------------------------------------")
                var1 = 1
                sys.exit(1)

            if 'search' in command and 'directory' in command and 'for' in command:
                print('STARTING SEARCH ...')
                search = command.split()[3]
                print("*****************")
                print('Search term: ')
                print(search)
                def find(name, path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            if file.startswith(search) or file.endswith(search):
                                print("------------------------")
                                print(os.path.join(root, file))
                                print("------------------------")
                                #FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
                                #path = os.path.normpath(path)
                                #subprocess.run([FILEBROWSER_PATH, root]) #root anstatt path ?
                                return os.path.join(root, name)
                find(search, 'C:/')
                find(search, 'D:/')
                time.sleep(3.0)
                var1 = 1
                sys.exit(1)

            Capture_speech()

        except:
            if var1 == 1:
                pass

            else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print('Sorry did not get that!')
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
                Capture_speech()

    Capture_speech()