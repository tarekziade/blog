Afpy Camp 2012
##############

:date: 2012-07-12 23:50
:tags: python, mozilla
:category: mozilla
:author: Tarek Ziade

.. image:: https://lh6.googleusercontent.com/-vjV0w0TuxRA/UAFlsFOY2eI/AAAAAAAACtg/gC_RBjaRhmo/w442-h331/afpycamp.gif
   :align: right

The Afpy Camp at my house is now over, and I had a great time as
usual. This year we decided we'd play with Raspberry Pi and Arduino
boards, so it was less Python-centric than usual.

.. image:: http://awesomeness.openphoto.me/custom/201207/6cf975-camp--1-of-3-_870x550.jpg
   :align: right

After a few basic LED projects, we tried (and failed) at making a LCD screen
work but it seems that there's a problem with the Leonardo board.
Overall that board seems to be quite buggy compared to the Uno.

I then worked with Alain on making a DC Motor run, using a transistor
and a battery pack for the motor. It took us quite some time but
we managed to make it work. The goal was to design a board to
control two engines to run an old RC Nikko car I stole from
my son's room. The board we planned to build was supposed to
send a negative or positive current into the engines, so the car
could move forward, backwards and on the sides.

But all this work became overkill because sunday, Laurent
brought a shield that does all this job (and more). It's a
shield you can plug on an Arduino Uno and that can control
4 DC engines and 2 servos.

So all we had to do is to plug it in the car, and write
a small program based on the **AFMotor** library.

We then added a bluetooth chip so we could control the
car from an Android phone using a Bluetooth terminal.

Here's the program uploaded in the Arduino::

    #include <AFMotor.h>
    #include <SoftwareSerial.h>

    AF_DCMotor motor(4, MOTOR12_64KHZ);
    AF_DCMotor motor2(2, MOTOR12_64KHZ);
    SoftwareSerial mySerial(14, 15);


    void setup() {
      Serial.begin(9600);
      mySerial.begin(9600);
      motor.setSpeed(255);
      motor2.setSpeed(255);
    }

    void loop() {
    int value =  mySerial.read();

    if (value != -1) {
        Serial.print(value);

        if (value==49) {
        motor.run(FORWARD);
        }

        if (value==50) {
        motor.run(BACKWARD);
        }

        if (value==51) {
        motor.run(RELEASE);
        }

        if (value==52) {
        motor2.run(FORWARD);
        }

        if (value==53) {
        motor2.run(BACKWARD);
        }

        if (value==54) {
        motor2.run(RELEASE);
        }
    }
  }


.. image:: http://awesomeness.openphoto.me/custom/201207/4adfe5-alexis-sing--1-of-1-_870x550.jpg
   :align: right

Pretty basic stuff: when we hit '1' on the phone -- char 59, the
car moves fowards, etc.

Here's a video of the car in motion: https://plus.google.com/106436370949746015255/posts/89ft1PokuNd

The next step would be to create an Phone application with a real UI.
Maybe based on the accelerometer. Ideally, I want to create a Boot to Gecko
(Firefox OS) application that does this. That's a good excuse to play with
this new system.

And ultimately, I'd like to add a webcam and build a small Python web
server so people can take control of the car over the web. But that's
another story.

Thanks a lot to http://hackspark.fr & Jon for all the hardware !

