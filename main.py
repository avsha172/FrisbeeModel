import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import math



def init_global_vars():
    global vy_stamp, vx_stamp, t_stamp, ax_stamp, x_stamp, y_stamp, ALPHA_stamp, ay_stamp
    vy_stamp = []
    vx_stamp = []
    t_stamp = []
    ax_stamp = []
    x_stamp = []
    y_stamp = []
    ALPHA_stamp = []
    ay_stamp = []

def simulation_handler(vy=0, vx=0, frisbee_angle=0, dt=1, y = 0, time_to_run = 1, is_visualize = False, QuiverRun = [0]):
    global vy_stamp, vx_stamp, t_stamp, ax_stamp, x_stamp, y_stamp, ALPHA_stamp, ay_stamp
    init_global_vars()
    frisbee_angle = frisbee_angle*math.pi/180
    m = 0.175
    p = 1.23
    AREA = 0.0568
    CL0 = 0.3331
    CLA = 1.9124
    CD0 = 0.1769
    CDA = 0.685
    ALPHA0 = -4 * math.pi / 180
    g = -9.81
    ax_Func = lambda vx, vy: -p * AREA / 2 * (np.power(vx,2)+np.power(vy,2)) * (math.cos(Teta)*Cd+Cl*math.sin(Teta)) / m
    ay_Func = lambda vx, vy: p * AREA / 2 * (np.power(vx,2)+np.power(vy,2)) * (math.cos(Teta)*Cl-Cd*math.sin(Teta)) / m+g
    ay = 0
    ax = 0
    x = 0
    t = -dt
    if (pow(vx, 2) + pow(vy, 2) != 0):
        Teta = math.acos(vx / pow(pow(vx, 2) + pow(vy, 2), 0.5)) * ((vy > 0) * 2 - 1)
    else:
        Teta = -90*math.pi/180
    while y >= 0:
        t += dt
        ALPHA = frisbee_angle - Teta
        Cl = CL0 + CLA * ALPHA
        Cd = CD0 + CDA * pow(ALPHA - ALPHA0, 2)
        ax = ax_Func(vx, vy)
        ay = ay_Func(vx, vy)
        appendItems(ax, ay, y, x, vy, vx, t, ALPHA)
        vx = vx + ax * dt
        vy = vy + ay * dt
        x = x + vx * dt
        y = y + vy * dt
        Teta = math.acos(vx / pow(pow(vx, 2) + pow(vy, 2), 0.5)) * ((vy > 0) * 2 - 1)
        if (t > time_to_run):
            print("didnt really end")
            break
        # print(x,y,ax,ay)
    if QuiverRun[0] > 0:
        t = 0
        new_ax_stamp = []
        new_ay_stamp = []
        new_vx_stamp = []
        new_vy_stamp = []
        vx = 0
        t = 0
        dt = QuiverRun[2]
        while QuiverRun[0] >= t:
            t += dt
            t2 = 0
            vy = 0
            while QuiverRun[1] >= t2:
                t2 = t2+dt
                ALPHA = frisbee_angle - Teta
                Cl = CL0 + CLA * ALPHA
                Cd = CD0 + CDA * pow(ALPHA - ALPHA0, 2)
                ax = ax_Func(vx, vy)
                ay = ay_Func(vx, vy)
                appendItemsQuiver(ax, ay, vx, vy,new_ax_stamp,new_ay_stamp,new_vx_stamp,new_vy_stamp)
                vy = vy + dt
                Teta = math.acos(vx / pow(pow(vx, 2) + pow(vy, 2), 0.5)) * ((vy > 0) * 2 - 1)
            vx = vx +dt
    if QuiverRun[0]>0:
        plt.quiver(new_vx_stamp, new_vy_stamp, new_ax_stamp, new_ay_stamp)
        plt.plot(x_stamp, y_stamp)
        plt.title('velocity in y direction in relation to x direction.\n Arrows are the acceleration of the frisbee')
        plt.ylabel('velocity of y direction')
        plt.xlabel('velocity of x direction')
        plt.show()
    elif is_visualize:
        an = np.linspace(0, 2 * np.pi, 100)
        # fig, axs = plt.subplots(1, 1)
        plt.figure(figsize=(6, 6))
        plt.scatter(x_stamp, y_stamp,s = 10, c=np.array(ALPHA_stamp)/math.pi*180, cmap='rainbow')
        plt.colorbar(label="color of the point is the value of the attack angle")
        an = np.linspace(0, 2 * np.pi, 100)
        # fig, axs = plt.subplots(1, 1)
        plt.figure(figsize=(15, 15))
        plt.plot(x_stamp, y_stamp)
        # plt.colorbar(label="color of the point is the value of the attack angle")
        plt.xlim(0,30)
        plt.ylim(0, 5)
        #axs.axis('equal')
        # axs.set(xlim=(0,55), ylim=(0,55))
        plt.title('The path of the frisbee')
        plt.ylabel('y direction')
        plt.xlabel('x direction')
        plt.show()
        # plt.plot(x_stamp,np.array(ALPHA_stamp)/math.pi*180)
        # plt.title('The attack angle in relation to x direction')
        # plt.ylabel('The attack angle')
        # plt.xlabel('The x direction')
        # plt.show()
    return x_stamp, y_stamp, np.array(ALPHA_stamp)/math.pi*180

def appendItemsQuiver(ax,ay,vx,vy,new_ax_stamp,new_ay_stamp,new_vx_stamp,new_vy_stamp):
    new_ay_stamp.append(ay)
    new_ax_stamp.append(ax)
    new_vy_stamp.append(vy)
    new_vx_stamp.append(vx)
def appendItems(ax, ay, y, x, vy, vx, t, ALPHA):
    global vy_stamp, vx_stamp, t_stamp, ax_stamp, x_stamp, y_stamp, ALPHA_stamp, ay_stamp
    ax_stamp.append(ax)
    ay_stamp.append(ay)
    y_stamp.append(y)
    x_stamp.append(x)
    vy_stamp.append(vy)
    vx_stamp.append(vx)
    t_stamp.append(t)
    ALPHA_stamp.append(ALPHA)


frisbee_angle = 0
simulation_handler(vy=-10, vx=20, frisbee_angle =
frisbee_angle, dt = 0.01, y=3, time_to_run=10, is_visualize=True, QuiverRun = [0,20,2])






# this is the animation part
#fps = 3
# V_start = 20
# writer = PillowWriter(fps=fps, metadata=metadata)
# metadata =  dict(title = 'Movie', artist = 'Moah')
#
# fig = plt.figure()
# frisbee_angle = 0
# with writer.saving(fig, "AttackAngle.gif", 100):
#     xlist, ylist, zlist = simulation_handler(vy=V_start * np.sin(frisbee_angle * math.pi / 180),
#                                              vx=V_start * np.cos(frisbee_angle * math.pi / 180), frisbee_angle=
#                                              frisbee_angle, dt=0.01, y=1, time_to_run=10, is_visualize=False,
#                                              QuiverRun=[0, 20, 2])
#     plt.scatter(xlist, ylist, s=10, c=zlist, cmap='rainbow')
#     plt.colorbar(label="color of the point is the value of the attack angle")
#     plt.title("animation of the path of the frisbee \n every line is a diffrent time the frisbee was thrown")
#     plt.xlabel("x direction fo firsbee")
#     plt.ylabel("y direction fo firsbee")
#     plt.clim(-4, 60)
#     writer.grab_frame()
#     for frisbee_angle in np.linspace(1,30,30):
#         xlist, ylist, zlist= simulation_handler(vy=V_start*np.sin(frisbee_angle*math.pi/180),
#                                                 V_start=20*np.cos(frisbee_angle*math.pi/180),
#                                                 frisbee_angle =frisbee_angle, dt = 0.01, y=1,
#                                                 time_to_run=10, is_visualize=False, QuiverRun = [0,20,2])
#         plt.scatter(xlist, ylist, s = 10, c=zlist, cmap='rainbow')
#         plt.clim(-4, 60)
#         writer.grab_frame()