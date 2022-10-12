from psychopy import visual, core, event, sound #import some libraries from PsychoPy
import psychopy.event
import os
from psychopy import data
from psychopy import event
from random import shuffle
import random, copy
import numpy as np



####################################################################################
####################################################################################
################################Subject Details#####################################
Sub=1
################################Experiment Details##################################
ExpNo=
####################################################################################
#####################how many image sets you wish to show the subject###############
N_set=
###########how many times you want to continue motor imagery experiment#############   
N=
###################display time of images in RSVP experiment########################
disp_dur=0.400#400ms
####################################################################################
####################################################################################





#Create window
win = visual.Window(color="black", size=[1920,1080],monitor='testMonitor',units='norm',screen=1,fullscr=True)
textQ = visual.TextStim(win,alignVert='top')




# #############################Primary Instructions################################
# #----------------------------------------Text------------------------------------
StartMessage = visual.TextStim(win, text='\t\tWELCOME\n \nSit Back And Relax',pos=(+0.70, 0.0),alignHoriz='center', alignVert='center', color="white")
StartMessage.draw()
win.flip()
core.wait(5.0)

Instructions1_text='CLOSE your EYES AFTER hearing the BEEP   \n\nOPEN your EYES when you hear another BEEP'
Instructions1 = visual.TextStim(win, text=Instructions1_text,pos=(+0.50, 0.0),alignHoriz='center', alignVert='center',  color="white")
Instructions1.draw()
win.flip()
core.wait(10.0)

##############EYE CLOSE###################
sound_1 = sound.Sound(secs=0.1, octave=4) 
sound_1.setVolume(1000)
sound_1.play()
win.flip()
core.wait(2.0)

win.flip()
core.wait(8.0)

#############EYE OPEN######################
sound_1 = sound.Sound(secs=0.1, octave=4) 
sound_1.setVolume(1000)
sound_1.play()
win.flip()
core.wait(2.0)

win.flip()
core.wait(8.0)

# sound_1 = sound.Sound(secs=0.1, octave=4) 
# sound_1.setVolume(1000)
# sound_1.play()
# win.flip()
# core.wait(2.0)

Instructions1_text='Relax'
Instructions1 = visual.TextStim(win, text=Instructions1_text,pos=(0.85, 0.0),alignHoriz='center', alignVert='center', color="white")
Instructions1.draw()
win.flip()
core.wait(4.0)

Instructions1_text='\t ARE YOU READY ?\n\nPress the SPACE bar to start the experiment'
Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.55, 0.0), height=0.11 , color="white")
Instructions1.draw()
win.flip()
response = event.waitKeys()





# # # ###########################RSVP###########################################
# # # ##########################################################################
# # # ##################################################
Instructions1_text='Now look at the black screen until you see' #\n\n\nDo not Blink'
Instructions1 = visual.TextStim(win, text=Instructions1_text,pos=(0.5, 0.2) , color="white")
Initial_stimulus='+'
Init_Stim = visual.TextStim(win, text=Initial_stimulus,bold=True,pos=(0.95, -0.2),height=0.25 , color="white")
Instructions1.draw()
Init_Stim.draw()
win.flip()
core.wait(6.0)

#display a blank screen
win.flip()
core.wait(3.0)


Initial_stimulus='+'
Init_Stim = visual.TextStim(win, text=Initial_stimulus,bold=True,pos=(0.95, 0.0),height=0.25 , color="white")
Init_Stim.draw()
win.flip()
core.wait(3.0)

# sound_1 = sound.Sound(secs=0.1, octave=4) 
# sound_1.setVolume(1000)
# sound_1.play()
# win.flip()
# core.wait(2.0)
s1='D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\ExpDatasets\\ImageSets720x1280'

target_marker=[]

#randomly pick N_set number of sets
set_indx=list(range(1,11))
print(set_indx)
random.shuffle(set_indx)
print(set_indx)

imagesets_displayed=[]

# Display the target-nontarget image sets
for count in range(1,N_set+1): 
    
    Init_Stim.draw()
    win.flip()
    core.wait(2.0)

    inp=list(range(1,111))
    random.shuffle(inp)
    print(inp)

    img_seq=[]

    target_marker=[]

    for i in range(110):#110
        # input_num=random.randint(1,110)
        input_num=inp[i]
        img_seq.append(input_num)
        input_path=os.path.join(s1,'Set'+str(set_indx[count-1]),'img'+str(input_num)+'.jpg')
        # input_path=os.path.join(s1,'Set'+str(10),'img'+str(input_num)+'.jpg')
        print(input_path)

        if input_num<=10:
            marker=1
        else:
            marker=0
            
        target_marker.append(marker)

        img = psychopy.visual.ImageStim(
            win=win,
            image=input_path,
            units="pix"
        )

        img.draw()

        win.flip()
        core.wait(disp_dur)#display images at a fraeme rate of 2 Hz.

    print(target_marker)
    print(len(target_marker))

    imagesets_displayed.append(set_indx[count])

    # display a blank screen
    win.flip()
    core.wait(12.0)

    s_tar=os.path.join('D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\target_markers\\S'+str(Sub),'rsvp_target_marker'+str(count)+'_S'+str(Sub)+'_Rec'+str(ExpNo))
    np.save((os.path.join(s_tar+'.npy')),target_marker)

    s_imgseq=os.path.join('D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\target_markers\\S'+str(Sub),'image_seq_'+str(count)+'_Set'+str(set_indx[count])+'_S'+str(Sub)+'_Rec'+str(ExpNo))
    print(s_imgseq)
    np.save((os.path.join(s_imgseq+'.npy')),img_seq)    

s_imagesets=os.path.join('D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\target_markers\\S'+str(Sub),'imagesets_displayed_S'+str(Sub)+'_Rec'+str(ExpNo))
print(s_imagesets)
np.save((os.path.join(s_imagesets+'.npy')),imagesets_displayed)




# # # ################################################Intermediate Instruction Sets#######################
# # # ####################################################################################################
Instructions1_text='READY to do some activities?\n\nPress the SPACE bar to start'
Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.55, 0.0), height=0.11 , color="white")
Instructions1.draw()
win.flip()

response = event.waitKeys()
KeyEvent=event.getKeys()

Instructions1_text='Relax'
Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.85, 0.0), height=0.15, color="white")
Instructions1.draw()
win.flip()
core.wait(5.0)

#display a blank screen
win.flip()
core.wait(2.0)




# ###############################################Motor Imagery##########################################
# ######################################################################################################
# ##################################################
Instructions_text='\t\tINSTRUCTIONS:\n\nWe will show you some videos'
Instructions = visual.TextStim(win, text=Instructions_text, pos=(0.60, 0.0), height=0.11, color="white")
Instructions.draw()
win.flip()
core.wait(5.0)

Instructions_text='\tINSTRUCTIONS:\n\nIMAGINE performing the ACTION as shown in video \n\n with CLOSED EYES\n\n\n OPEN your EYES when you hear another BEEP'
Instructions = visual.TextStim(win, text=Instructions_text, pos=(0.6, 0.0), height=0.11,  color="white")
Instructions.draw()
win.flip()
core.wait(10.0)

#display a blank screen
win.flip()
core.wait(2.0)

Instructions1_text='\t ARE YOU READY ?\n\nPress the SPACE bar to start'
Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.55, 0.0), height=0.11 , color="white")
Instructions1.draw()
win.flip()
response = event.waitKeys()

##--------------------------------Instructions List--------------------------------------##

Movement_text1='\t\t\t\tIMAGINE\n\nMoving Right Arm\nto Front'#'\n\nafter seeing +'
Movement_text1_1='\t\t\t MOVE\n\nRight Arm to Front'

Movement_text2='\t\t\t\tIMAGINE\n\nMoving Left Arm\nto Front'
Movement_text2_1='\t\t\t MOVE\n\nLeft Arm to Front'

Movement_text3='\t\t\t\tIMAGINE\n\nMoving Right Arm\nto Right'
Movement_text3_1='\t\t\t MOVE\n\nRight Arm to Right'

Movement_text4='\t\t\t\tIMAGINE\n\nMoving Left Arm\nto Left' 
Movement_text4_1='\t\t\t MOVE\n\nLeft Arm \nto Left' 
                          
Movement_text5='\t\t\t\tIMAGINE\n\nMoving Right Leg \nto Front' 
Movement_text5_1='\t\t\t MOVE\n\nRight Leg to Front'

Movement_text6='\t\t\t\tIMAGINE\n\nMoving Left Leg \nto Front' 
Movement_text6_1='\t\t\t MOVE\n\nLeft Leg to Front'

Movement_text7='\t\t\t\tIMAGINE\n\nMoving Right Leg\nto Right' 
Movement_text7_1='\t\t\t MOVE\n\nRight Leg to Right'
 
Movement_text8='\t\t\t\tIMAGINE\n\nMoving Left Leg\nto Left' 
Movement_text8_1='\t\t\t MOVE\n\nLeft Leg to Left'

M=[Movement_text1, Movement_text1_1, Movement_text2, Movement_text2_1, Movement_text3, Movement_text3_1,
    Movement_text4, Movement_text4_1, Movement_text5, Movement_text5_1, Movement_text6, Movement_text6_1,
    Movement_text7, Movement_text7_1, Movement_text8, Movement_text8_1]
print(len(M))

target_marker=[]
MotorImagery_seq=[]
MotorMovements_seq=[]

##------------------------------------create index for all the list of videos------------------##
indx= list(range(1,9))
print(indx)

random.shuffle(indx)
print(indx)


##------------------------ Run all the videos once first time---------------------------##
for i in range (len(indx)+1):#len(indx)+1):
    vid_indx=indx[i-1]

    #display a blank screen
    win.flip()
    core.wait(2.0)

    filename1='D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\ExpDatasets\\MotorMovementsCoded\\'+str(vid_indx)+'.mp4'
    mov = visual.MovieStim3(win, filename =filename1, flipVert=False,noAudio=True)#, autoDraw=True)
    print('ShowingVideo',vid_indx,':',mov.duration, ' seconds')
    while mov.status != visual.FINISHED:
            #Play movie
            mov.draw()
            win.flip()

    # mov = visual.MovieStim3(win, filename =filename1, flipVert=False,noAudio=True)
    # while mov.status != visual.FINISHED:
            # #Play movie
            # mov.draw()
            # win.flip()

    #display a blank screen
    win.flip()
    core.wait(2.0)

    Movement_text=M[2*vid_indx-2]+'\n\n\nafter hearing the BEEP'
    Movement = visual.TextStim(win, text=Movement_text, pos=(0.60, 0.0), height=0.12,  color="white")
    Movement.draw()
    win.flip()
    core.wait(6.0)

    close_eye_text= '\t \tClose your eyes'
    close_eye = visual.TextStim(win, text=close_eye_text, pos=(0.60, 0.0), height=0.12,  color="white")
    close_eye.draw()
    win.flip()
    core.wait(3.0)

    sound_1 = sound.Sound(secs=0.1, octave=4) 
    sound_1.setVolume(1000)
    sound_1.play()
    win.flip()
    core.wait(2.0)

    marker=800+vid_indx
    MotorImagery_seq.append(marker)
   

    #perform action
    win.flip()
    core.wait(3.0)

    

    sound_1 = sound.Sound(secs=0.1, octave=4) 
    sound_1.setVolume(1000)
    sound_1.play()
    win.flip()
    core.wait(2.0)

    #display a blank screen
    win.flip()
    core.wait(5.0)

    #perform the motor imagery action after the '+''stimulus
    
    Movement1_text=M[2*vid_indx-1]
    Movement1 = visual.TextStim(win, text=Movement1_text, pos=(0.60, 0.0), height=0.12,  color="white")
    Movement1.draw()
    win.flip()
    core.wait(6.0)

    # #perform the motor imagery action after the '+''stimulus
    Initial_stimulus='+'
    Init_Stim = visual.TextStim(win, text=Initial_stimulus,bold=True,pos=(0.95, 0.0),height=0.25 , color="white")
    Init_Stim.draw()

 
    win.flip()
    core.wait(2.0)

    marker=810+vid_indx
    MotorMovements_seq.append(marker)
    # target_marker.append(marker)

    #perform action
    win.flip()
    core.wait(3.0)

    End_stimulus='...'
    End_stimulus = visual.TextStim(win, text=End_stimulus, pos=(1.0, 0.0), height=0.15, color="white")
    End_stimulus.draw()
    win.flip()
    core.wait(1.5)

    Instructions1_text='Relax '
    Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.85, 0.0), height=0.15, color="white")
    Instructions1.draw()
    win.flip()
    core.wait(10.0)


Instructions1_text='Do you want to continue?\n\nPress the SPACE bar to start'
Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.55, 0.0), height=0.11 , color="white")
Instructions1.draw()
win.flip()
response = event.waitKeys()

Instructions1_text='Relax '
Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.85, 0.0), height=0.15, color="white")
Instructions1.draw()
win.flip()
core.wait(2.0)


##------------------------ Run the videos in random fashion and ask to perform---------------------------##
for i in range (N):
    vid_indx1=random.randint(1,len(indx))
    print(vid_indx1)

    # #display a blank screen
    # win.flip()
    # core.wait(2.0)

    filename1='D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\ExpDatasets\\MotorMovementsCoded\\'+str(vid_indx1)+'.mp4'
    mov = visual.MovieStim3(win, filename =filename1, flipVert=False,noAudio=True)#, autoDraw=True)
    print('ShowingVideo',vid_indx1,':',mov.duration, ' seconds')
    while mov.status != visual.FINISHED:
            #Play movie
            mov.draw()
            win.flip()


    #display a blank screen
    win.flip()
    core.wait(2.0)

    Movement_text=M[2*vid_indx1-2]+'\n\n\nafter hearing the BEEP'
    Movement = visual.TextStim(win, text=Movement_text, pos=(0.60, 0.0), height=0.12,  color="white")
    # Movement = visual.TextStim(win, text=Movement_text, pos=(0.70, 0.0), height=0.15,  color="white")
    Movement.draw()
    win.flip()
    core.wait(5.0)

   
    marker=800+vid_indx1
    MotorImagery_seq.append(marker)
    #target_marker.append(marker)

    close_eye_text= '\t \tClose your eyes'
    close_eye = visual.TextStim(win, text=close_eye_text, pos=(0.60, 0.0), height=0.12,  color="white")
    close_eye.draw()
    win.flip()
    core.wait(3.0)

    sound_1 = sound.Sound(secs=0.1, octave=4) 
    sound_1.setVolume(1000)
    sound_1.play()
    win.flip()
    core.wait(2.0)


    #perform action
    win.flip()
    core.wait(3.0)

  
    sound_1 = sound.Sound(secs=0.1, octave=4) 
    sound_1.setVolume(1000)
    sound_1.play()
    win.flip()
    core.wait(2.0)

    #display a blank screen
    win.flip()
    core.wait(2.0)

    Movement1_text=M[2*vid_indx1-1]
    Movement1 = visual.TextStim(win, text=Movement1_text, pos=(0.60, 0.0), height=0.12,  color="white")
    # Movement1 = visual.TextStim(win, text=Movement1_text, pos=(0.70, 0.0), height=0.15, color="white")
    Movement1.draw()
    win.flip()
    core.wait(5.0)

    #perform the motor imagery action after the '+''stimulus
    Initial_stimulus='+'
    Init_Stim = visual.TextStim(win, text=Initial_stimulus,bold=True,pos=(0.95, 0.0),height=0.25 , color="white")
    Init_Stim.draw()


    win.flip()
    core.wait(2.0)

    marker=810+vid_indx1
    MotorMovements_seq.append(marker)
    #target_marker.append(marker)

    #perform action
    win.flip()
    core.wait(3.0)

    End_stimulus='...'
    End_stimulus = visual.TextStim(win, text=End_stimulus, pos=(1.0, 0.0), height=0.15, color="white")
    End_stimulus.draw()
    win.flip()
    core.wait(1.5)

    Instructions1_text='Relax '
    Instructions1 = visual.TextStim(win, text=Instructions1_text, pos=(0.85, 0.0), height=0.15, color="white")
    Instructions1.draw()
    win.flip()
    core.wait(10.0)


##-------------------------------------save the marker array------------------------------------------##
print(MotorImagery_seq)
print(MotorMovements_seq)
s_motorimagery=os.path.join('D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\target_markers\\S'+str(Sub),'MotorImagerySeq_S'+str(Sub)+'_Rec'+str(ExpNo))
np.save((os.path.join(s_motorimagery+'.npy')),MotorImagery_seq)
s_motormovement=os.path.join('D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\target_markers\\S'+str(Sub),'MotorMovementSeq_S'+str(Sub)+'_Rec'+str(ExpNo))
np.save((os.path.join(s_motormovement+'.npy')),MotorMovements_seq)



#####################################################################################################
##########################################End Instructions###########################################
thanks_text='Thanks for your patience\n\n  Have a Good Day'
Instructions1 = visual.TextStim(win, text=thanks_text,pos=(+0.60, 0.0),alignHoriz='center', alignVert='center',  color="white")
Instructions1.draw()
win.flip()
core.wait(3.0)

response = event.waitKeys()
KeyEvent=event.getKeys()    


x=np.load('D:\\BCI\\Experiments_Design\\Psychopy\\PsychopyExperiments\\RSVP_MI_combined\\target_markers\\S1\\imagesets_displayed.npy')
print(x)