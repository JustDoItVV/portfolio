import numpy as np
import matplotlib.pyplot as plt

# Functions for soil parameters estimation calculating

def unit_weight_estimation(vr_velocity, z_depth):
    return 0.7 * np.log(vr_velocity ** 5.16 / z_depth) + 0.17


def dynamic_shear_modulus(y_weight, vr_velocity):
    return 1.1 * 1e-6 * (y_weight * 1000 / 9.81) * vr_velocity ** 2


def transition_factor(y_weight):
    return 0.12 + np.exp(-0.68 * y_weight + 10)


def cohesion(y_weight, vr_velocity):
    return 4.2 * 1e-10 * (y_weight * 1000 / 9.81) * vr_velocity ** 2 + 0.0087


def friction_angle(vr_velocity, vp_velocity):
    return 45.6 - 7.6 * vp_velocity / vr_velocity


def p_wave_estimation(v_dyn_ratio, vr_velocity):
    return 1.05 * vr_velocity * ((2 * (1 - v_dyn_ratio) / (1 - 2 * v_dyn_ratio)) ** 0.5)


def ultimate_deviatoric_stress(c_cohesion, phi_angle, y_weight, z_depth, rf=0.9):
    phi_angle = np.radians(phi_angle)
    return ((c_cohesion * 1000 * (np.tan(phi_angle) ** (-1)) + (1 - np.sin(phi_angle)) * y_weight * z_depth) * (2 * np.sin(phi_angle)) / (1 - np.sin(phi_angle))) / rf


def elistic_modulus(e_modulus, r=0.65):
    return e_modulus / r


def hyperbolic_model(x, e_elastic, s_dev_elt):
    return x / (1 / (e_elastic) + x / (s_dev_elt * 0.001))


def graph(s_dev_elt, e_elastic, x_range):
    x = np.array(x_range)
    y = hyperbolic_model(x, e_elastic, s_dev_elt)
    plt.plot(x, y)
    plt.title('Model deformation curve')
    plt.xlabel('Relative strains, e1')
    plt.ylabel('Deviatoric stress, s_dev (MPa)')
    plt.show()
    return x, y


# 1st method: Deformation modulus estimation by MASW results
def main():
    print('Enter the Rayleigh wave velocity (m/s) and depth (m) separated by space:')
    vr_velocity, z_depth = map(float, input().split(' '))
    print('Enter soil unit weight (kN/m3). If you don\' have info about the weight, enter "estimate"')
    s = str(input())
    while True:
        try:
            s = float(s)
            break
        except Exception:
            if s == 'estimate':
                s = unit_weight_estimation(vr_velocity, z_depth)
                print(f'Estimated unit weight is {s:.3f} kN/m3')
                break
            else:
                print('Incorrect input. Try again')
        s = str(input())
    y_weight = s
    g0_dyn_modulus = dynamic_shear_modulus(y_weight, vr_velocity)
    print(f'G0 dynamic shear modulus is {g0_dyn_modulus:.0f} MPa')
    kg = transition_factor(y_weight)
    print(f'kG transition factor is {kg:.3f}')
    e_modulus = kg * g0_dyn_modulus
    print(f'E deformation modulus is {e_modulus:.1f} MPa')
    return [vr_velocity, z_depth, y_weight, g0_dyn_modulus, e_modulus]


# 2nd method: Model deformation curve plotting by MASW results
def model_deformation_curve(arr):
    print('Enter longitudinal wave velocity Vp. If you don\' have it, enter "estimate"')
    s = str(input())
    while True:
        try:
            s = float(s)
            break
        except Exception:
            if s == 'estimate':
                print('Enter assumed dynamic Poissons\'s ratio')
                v_dyn_ratio = str(input())
                while True:
                    try:
                        v_dyn_ratio = float(v_dyn_ratio)
                        break
                    except Exception:
                        print('Incorrect input. Try again')
                    v_dyn_ratio = str(input())
                s = p_wave_estimation(v_dyn_ratio, arr[0])
                print(f'Estimated P-wave velocity Vp is {s:.0f} m/s')
                break
            else:
                print('Incorrect input. Try again')
        s = str(input())
    vp_velocity = s
    c_cohesion = cohesion(arr[2], arr[0])
    print(f'c cohesion is {c_cohesion:.3f} MPa')
    phi_angle = friction_angle(arr[0], vp_velocity=vp_velocity)
    print(f'ф friction angle is {phi_angle:.1f} grad')
    s_dev_elt = ultimate_deviatoric_stress(c_cohesion, phi_angle, arr[2], arr[1], rf=0.9)
    print(f'S_dev ultimate deviatoric stress is {s_dev_elt:.3f} kPa')
    e_elastic = elistic_modulus(arr[4])
    print(f'E_el elastic deformation modulus is {e_elastic:.3f} MPa')
    x, y = graph(s_dev_elt, e_elastic, np.arange(0.001, 0.15, 0.01))


while True:
    arr = main()
    print('Plot the model deformation curve? (y/n) (Additional inputs required)')
    if input().strip() == 'y':
        model_deformation_curve(arr)
    print('Repeat the program? (y/n)')
    if input().strip() != 'y':
        break

