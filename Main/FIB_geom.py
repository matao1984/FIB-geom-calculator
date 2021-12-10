# -*- coding: utf-8 -*-

#
#
# Created by: PyQt5 UI code generator 5.12.3
#
#FIB needle rotation calculator v0.1
#Written by Tao Ma, taoma@umich.edu


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import matplotlib
matplotlib.use('Qt5Agg')
#%from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider, Button


class Ui_geom_cal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_geom_cal,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        
    def setupUi(self, GeomCal):
        GeomCal.setObjectName("GeomCal")
        GeomCal.resize(800, 233)
        self.label = QtWidgets.QLabel(GeomCal)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(GeomCal)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 141, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(GeomCal)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 31, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(GeomCal)
        self.label_3.setGeometry(QtCore.QRect(290, 40, 451, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(GeomCal)
        self.label_4.setGeometry(QtCore.QRect(220, 40, 55, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(GeomCal)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 140, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(GeomCal)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 70, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(GeomCal)
        self.label_6.setGeometry(QtCore.QRect(220, 70, 55, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(GeomCal)
        self.label_7.setGeometry(QtCore.QRect(290, 70, 451, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(GeomCal)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(GeomCal)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 100, 31, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(GeomCal)
        self.label_9.setGeometry(QtCore.QRect(220, 100, 55, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(GeomCal)
        self.label_10.setGeometry(QtCore.QRect(290, 100, 500, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(GeomCal)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(GeomCal)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 130, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_12 = QtWidgets.QLabel(GeomCal)
        self.label_12.setGeometry(QtCore.QRect(220, 130, 55, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(GeomCal)
        self.label_13.setGeometry(QtCore.QRect(290, 130, 510, 20))
        self.label_13.setObjectName("label_13")
        self.pushButton_1 = QtWidgets.QPushButton(GeomCal)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 160, 131, 41))
        self.pushButton_1.setObjectName("pushButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(GeomCal)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 160, 131, 41))
        self.pushButton_2.setObjectName("pushButton_3")
        self.label_14 = QtWidgets.QLabel(GeomCal)
        self.label_14.setGeometry(QtCore.QRect(170, 160, 261, 41))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(GeomCal)
        self.label_15.setGeometry(QtCore.QRect(600, 160, 141, 41))
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(GeomCal)
        self.label_19.setGeometry(QtCore.QRect(160, 210, 510, 16))
        self.label_19.setObjectName("label_19")

        self.retranslateUi(GeomCal)
        QtCore.QMetaObject.connectSlotsByName(GeomCal)

#=======Connect all the functions=============================================

        self.pushButton_1.clicked.connect(self.view_geom)
        self.pushButton_2.clicked.connect(self.geom_free_rotation)

    def retranslateUi(self, GeomCal):
        _translate = QtCore.QCoreApplication.translate
        GeomCal.setWindowTitle(_translate("geom_cal", "FIB Geometry Calculator v0.1"))
        self.label.setText(_translate("geom_cal", "Geometry setting"))
        self.label_2.setText(_translate("geom_cal", "Ion-beam offset angle"))
        self.lineEdit.setText(_translate("geom_cal", "52"))
        self.label_3.setText(_translate("geom_cal", "The angle between the ion beam and e-beam, usually 52  on TFS FIBs."))
        self.label_4.setText(_translate("geom_cal", "Degrees"))
        self.label_5.setText(_translate("geom_cal", "Needle insertion angle"))
        self.lineEdit_2.setText(_translate("geom_cal", "45"))
        self.label_6.setText(_translate("geom_cal", "Degrees"))
        self.label_7.setText(_translate("geom_cal", "TFS Helios G4/PFIB: 45; TFS Helios G3/650 or older models: 50."))
        self.label_8.setText(_translate("geom_cal", "Sample tilt"))
        self.lineEdit_3.setText(_translate("geom_cal", "0"))
        self.label_9.setText(_translate("geom_cal", "Degrees"))
        self.label_10.setText(_translate("geom_cal", "Equal to the stage tilt when the lamella is welded and lifted out by the easyLift."))
        self.label_11.setText(_translate("geom_cal", "Needle rotation angle"))
        self.lineEdit_4.setText(_translate("geom_cal", "0"))
        self.label_12.setText(_translate("geom_cal", "Degrees"))
        self.label_13.setText(_translate("geom_cal", "Rotate the needle to see the geometry. Positive number rotates counterclockwise."))
        self.pushButton_1.setText(_translate("geom_cal", "View"))
        self.pushButton_2.setText(_translate("geom_cal", "Free rotation"))
        self.label_14.setText(_translate("geom_cal", "View the geometry with the above settings."))
        self.label_15.setText(_translate("geom_cal", "Rotate the needle live!"))
        self.label_19.setText(_translate("geom_cal", "FIB geometry calculator v0.1 Released: 12/9/2021 by Dr. Tao Ma taoma@umich.edu"))


#=================== Define botton functions =================================
    def view_geom(self):
        #Set up the original geometry
        N_theta = float(self.lineEdit_2.text()) #Needle insertion angle in degree. PFIB: 45; Helios 650/G3: 50
        N_theta_r = math.radians(N_theta)
        I_ang = float(self.lineEdit.text()) #Ion-beam offset angle from the e-beam
        S_x, S_y = 10, 5 #A rectangle TEM lamella, 10 x 5 in arb. unit
        Tilt = float(self.lineEdit_3.text())
        #Sample tilt relative to the y-z plane, equivalent to the stage tilt
        Tilt_r = math.radians(Tilt)
        #Calculate the coordinates of the sample
        A = (-S_y * math.sin(Tilt_r), 0, -S_y * math.cos(Tilt_r))
        B = (-S_y * math.sin(Tilt_r), S_x, -S_y * math.cos(Tilt_r))
        C = (0, S_x, 0)
        l = 10 #Needle length in arb. unit
        N_A = (0, 0, 0)#Needle point A at the origin
        N_B = (0, -l*math.cos(N_theta_r), l*math.sin(N_theta_r))#Needle point B
        
        N_a = float(self.lineEdit_4.text()) #Needle rotation angle
        
        #Apply rotation for A, B, and C
        A1 = coo_rot(A, N_a, N_theta)
        B1 = coo_rot(B, N_a, N_theta)
        C1 = coo_rot(C, N_a, N_theta)
        
        title = 'Geometry after rotating the needle by {} degrees'.format(N_a)
        plot_view(A1, B1, C1, N_A, N_B, title, I_ang)
        
        plt.show()
        
        
    def geom_free_rotation(self):
        #Set up the original geometry
        N_theta = float(self.lineEdit_2.text()) #Needle insertion angle in degree. PFIB: 45; Helios 650/G3: 50
        N_theta_r = math.radians(N_theta)
        I_ang = float(self.lineEdit.text()) #Ion-beam offset angle from the e-beam
        S_x, S_y = 10, 5 #A rectangle TEM lamella, 10 x 5 in arb. unit
        Tilt = float(self.lineEdit_3.text())
        #Sample tilt relative to the y-z plane, equivalent to the stage tilt
        Tilt_r = math.radians(Tilt)
        #Calculate the coordinates of the sample
        A = (-S_y * math.sin(Tilt_r), 0, -S_y * math.cos(Tilt_r))
        B = (-S_y * math.sin(Tilt_r), S_x, -S_y * math.cos(Tilt_r))
        C = (0, S_x, 0)
        l = 10 #Needle length in arb. unit
        N_A = (0, 0, 0)#Needle point A at the origin
        N_B = (0, -l*math.cos(N_theta_r), l*math.sin(N_theta_r))#Needle point B
        
        #Add a slider for easy viewing
        # Define initial parameters
        N_ini = 0
        # Create the figure and the line that we will manipulate
        title = 'Free needle rotation with the slider'
        fig4, ax1, ax2, ax3, ax4, ax5, line1, line2, line3, line4, line5 = plot_view(A, B, C, N_A, N_B, title, I_ang)
        
        
        # adjust the main plot to make room for the sliders
        plt.subplots_adjust(bottom=0.25)
        
        # Make a horizontal slider to control the frequency.
        ax_ang = plt.axes([0.25, 0.1, 0.65, 0.03])
        ang_slider = Slider(
            ax=ax_ang,
            label='Rotation (degree)',
            valmin=0,
            valmax=360,
            valinit=N_ini,
        )
        # The function to be called anytime a slider's value changes
        def update(val):
            A1 = coo_rot(A, ang_slider.val, N_theta)
            B1 = coo_rot(B, ang_slider.val, N_theta)
            C1 = coo_rot(C, ang_slider.val, N_theta)
            x1, y1, z1 = zip((0,0,0), A1, B1, C1, (0,0,0))
            line1.set_data_3d(x1, y1, z1)
            line2.set_data_3d(x1, y1, z1)
            line3.set_data_3d(x1, y1, z1)
            line4.set_data_3d(x1, y1, z1)
            line5.set_data_3d(x1, y1, z1)
            fig4.canvas.draw_idle()
            
        # register the update function with the slider
        ang_slider.on_changed(update)
        
        # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
        resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
        button = Button(resetax, 'Reset', hovercolor='0.975')
        
        def reset(event):
            ang_slider.reset()
            
        button.on_clicked(reset) 
        resetax._button = button #Create a dummy reference to hold the button variable
        
        plt.show()


#==================== Modules and helper functions ===================================


#Define a coordinate calculation function for needle rotation
def coo_rot(A, n, N_theta): #A: Coordinate (x,y,z); n: Needle rotation anle in degree (counterclockwise)
    #Define rotation matrix for needle rotation
    #First, rotate the needle clockwise by 90-N_theta to align the z axis
    r1 = math.radians(90 - N_theta) #Rotation angle for this operation
    R1 = [[1, 0, 0],[0, math.cos(-r1), -math.sin(-r1)],[0,math.sin(-r1),math.cos(-r1)]]#Rotation matrix by counterclockwise by -r1
    #Then, rotate along the z axis counterclockwise by a desired angle (Needle rotation angle)
    r2 = math.radians(n)
    R2 = [[math.cos(r2), -math.sin(r2), 0], [math.sin(r2), math.cos(r2), 0], [0, 0, 1]]
    #Finally, rotate the needle counterclockwise by 90-N_theta back to the original direction
    R3 = [[1, 0, 0],[0, math.cos(r1), -math.sin(r1)],[0, math.sin(r1), math.cos(r1)]]
    #Apply the rotation
    A1 = np.dot(R1,A)
    A2 = np.dot(R2,A1)
    A3 = np.dot(R3,A2)
    return A3

#Define a function for easy plotting
def plot_view(A, B, C, N_A, N_B, title, I_ang):
    fig = plt.figure(dpi=150) #Create 2 x 3 subplots
    ax1 = fig.add_subplot(2, 3, 1, projection='3d', proj_type='ortho')
    fig.suptitle(title)
    x, y, z = zip(N_A, A, B, C, N_A)
    
    #Geometry view
    ax1.view_init(azim=10, elev=20)
    ax1.set_box_aspect([1,1,1])
    ax1.plot3D((N_A[0],N_B[0]),(N_A[1],N_B[1]),(N_A[2],N_B[2]),'b')
    line1, = ax1.plot3D(x, y, z, 'r')
    ax1.set_xlim(-8,8)
    ax1.set_ylim(-3,13)
    ax1.set_zlim(-11,5)
    ax1.set_title('Geometry')
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.set_zticklabels([])

    #Front view
    ax2 = fig.add_subplot(2,3,2, projection='3d', proj_type='ortho')
    line2, = ax2.plot3D(x, y, z, 'r')
    ax2.view_init(azim=0, elev=0)
    ax2.set_box_aspect([1,1,1])
    ax2.plot3D((N_A[0],N_B[0]),(N_A[1],N_B[1]),(N_A[2],N_B[2]),'b')
    ax2.set_xlim(-8,8)
    ax2.set_ylim(-3,13)
    ax2.set_zlim(-11,5)
    ax2.set_title('Front View')
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.set_zticklabels([])
    #Side view
    ax3 = fig.add_subplot(2,3,3, projection='3d', proj_type='ortho')
    line3, = ax3.plot3D(x, y, z, 'r')
    ax3.view_init(azim=-90, elev=0)
    ax3.set_box_aspect([1,1,1])
    ax3.plot3D((N_A[0],N_B[0]),(N_A[1],N_B[1]),(N_A[2],N_B[2]),'b')
    ax3.set_xlim(-8,8)
    ax3.set_ylim(-3,13)
    ax3.set_zlim(-11,5)
    ax3.set_title('Side View')
    ax3.set_xticklabels([])
    ax3.set_yticklabels([])
    ax3.set_zticklabels([])
    
    #E-beam view
    ax4 = fig.add_subplot(2,3,4, projection='3d', proj_type='ortho')
    line4, = ax4.plot3D(x, y, z, 'r')
    ax4.view_init(azim=0, elev=-90)
    ax4.set_box_aspect([1,1,1])
    ax4.plot3D((N_A[0],N_B[0]),(N_A[1],N_B[1]),(N_A[2],N_B[2]),'b')
    ax4.set_xlim(-8,8)
    ax4.set_ylim(-3,13)
    ax4.set_zlim(5,-11)
    ax4.set_title('E-beam View')
    ax4.set_xticklabels([])
    ax4.set_yticklabels([])
    ax4.set_zticklabels([])
    
    #Ion-beam View
    ax5 = fig.add_subplot(2,3,5, projection='3d', proj_type='ortho')
    line5, = ax5.plot3D(x, y, z, 'r')
    ax5.view_init(azim=0, elev=-(90-I_ang))
    ax5.set_box_aspect([1,1,1])
    ax5.plot3D((N_A[0],N_B[0]),(N_A[1],N_B[1]),(N_A[2],N_B[2]),'b')
    ax5.set_xlim(-8,8)
    ax5.set_ylim(-3,13)
    ax5.set_zlim(5,-11)
    ax5.set_title('Ion-beam View')
    ax5.set_xticklabels([])
    ax5.set_yticklabels([])
    ax5.set_zticklabels([])
    return fig, ax1, ax2, ax3, ax4, ax5, line1, line2, line3, line4, line5


#====Application entry==================================
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GeomCal = QtWidgets.QWidget()
    ui = Ui_geom_cal()
    ui.setupUi(GeomCal)
    GeomCal.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
