#Assignment No: 5
#Problem Statement :Understanding the connectivity of Raspberry-Pi /Beagle board circuit with
#IR sensor. Write an application to detect obstacles and notify the user using LEDs.


#===========================================================================================
#NAME     : priyanka chavan
#CLASS    : TE(A)
#ROLL NO. : 09
#SUBJECT  : ESIOT Lab.
#===============================================================================================

#    Assignment no: 5
#-----------------------------------------------------------------------------------------------
#Problem Statement :Understanding the connectivity of Raspberry-Pi /Beagle board circuit with
#IR sensor. Write an application to detect obstacles and notify the user using LEDs.

#================================================================================================
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN)



while True :
    prox_val = GPIO.input(36)
    if prox_val :
        print("obstacle detected\n")
        
    else :
        print("No obstacle detected\n")
       
        
