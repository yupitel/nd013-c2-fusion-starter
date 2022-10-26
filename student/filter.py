# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        self.dim_state = params.dim_state # process model dimension
        self.dt = params.dt # time increment
        self.q= params.q # process noise variable for Kalman filter Q

        self.F()
        self.Q()

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        dim = self.dim_state
        hdim = int(dim / 2)
        F = np.matrix(np.identity(dim))
        for i in range(0, hdim):
            F[i, hdim + i] = self.dt
        

        return F
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############

        q = self.q
        dt = self.dt
        q1 = ((dt**3)/3) * q 
        q2 = ((dt**2)/2) * q 
        q3 = dt * q
        dim = self.dim_state
        hdim = int(dim / 2)
        Q = np.zeros((dim, dim))
        for i in range(0, hdim):
            Q[i][i] = q1
            Q[i + hdim][i] = q2
            Q[i][i + hdim] = q2
            Q[i + hdim][i + hdim] = q3

        print(Q)

        return Q
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############

        F = self.F()
        x = F * track.x # state prediction
        P = F * track.P * F.transpose() + self.Q() # covariance prediction

        track.set_x(x)
        track.set_P(P)

        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        H = meas.sensor.get_H(track.x) # measurement matrix
        P = track.P
        gamma = self.gamma(track, meas) # residual
        S = self.S(track, meas, H) # covariance of residual
        K = P * H.transpose() * np.linalg.inv(S) # Kalman gain
        x = track.x + K * gamma # state update
        I = np.identity(self.dim_state)
        P = (I - K * H) * P # covariance update

        track.set_x(x)
        track.set_P(P)

        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        H = meas.sensor.get_H(track.x)
        gamma = meas.z - H * track.x

        return gamma

        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        H = meas.sensor.get_H(track.x)
        S = H * track.P * H.transpose() + meas.R

        return S
        
        ############
        # END student code
        ############ 