import pygame

class Keyboard:
    def __init__(self):
        self.pressed = [0,]*1000
        self.released = [0,]*1000

    def left_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return True
        return False

    def right_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            return True
        return False

    def up_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return True
        return False

    def down_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            return True
        return False

    def space_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        return False

    def enter_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        return False

    def w_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return True
        return False

    def a_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            return True
        return False

    def s_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            return True
        return False

    def d_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            return True
        return False

    def shift_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
            return True
        return False

    def tab_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            return True
        return False

    def q_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            return True
        return False

    def e_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            return True
        return False

    def r_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return True
        return False

    def t_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            return True
        return False

    def y_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            return True
        return False

    def u_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u]:
            return True
        return False

    def i_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i]:
            return True
        return False

    def o_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:
            return True
        return False

    def p_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            return True
        return False

    def f_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            return True
        return False

    def g_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            return True
        return False

    def h_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_h]:
            return True
        return False

    def j_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            return True
        return False

    def k_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            return True
        return False

    def l_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            return True
        return False

    def z_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            return True
        return False

    def x_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:
            return True
        return False

    def c_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            return True
        return False

    def v_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_v]:
            return True
        return False

    def b_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            return True
        return False

    def n_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            return True
        return False

    def m_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            return True
        return False

    def j_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            return True
        return False




    def space_is_pressed(self):
        if self.pressed[pygame.K_SPACE]:
            return True
        return False

    def space_is_released(self):
        if self.released[pygame.K_SPACE]:
            return True
        return False

    def a_is_pressed(self):
        if self.pressed[pygame.K_a]:
            return True
        return False

    def a_is_released(self):
        if self.released[pygame.K_a]:
            return True
        return False

    def b_is_pressed(self):
        if self.pressed[pygame.K_b]:
            return True
        return False

    def b_is_released(self):
        if self.released[pygame.K_b]:
            return True
        return False
    def c_is_pressed(self):
        if self.pressed[pygame.K_c]:
            return True
        return False

    def c_is_released(self):
        if self.released[pygame.K_c]:
            return True
        return False
    def d_is_pressed(self):
        if self.pressed[pygame.K_d]:
            return True
        return False

    def d_is_released(self):
        if self.released[pygame.K_d]:
            return True
        return False
    def e_is_pressed(self):
        if self.pressed[pygame.K_e]:
            return True
        return False

    def e_is_released(self):
        if self.released[pygame.K_e]:
            return True
        return False
    def f_is_pressed(self):
        if self.pressed[pygame.K_f]:
            return True
        return False

    def f_is_released(self):
        if self.released[pygame.K_f]:
            return True
        return False
    def g_is_pressed(self):
        if self.pressed[pygame.K_g]:
            return True
        return False

    def g_is_released(self):
        if self.released[pygame.K_g]:
            return True
        return False
    def h_is_pressed(self):
        if self.pressed[pygame.K_h]:
            return True
        return False

    def h_is_released(self):
        if self.released[pygame.K_h]:
            return True
        return False
    def i_is_pressed(self):
        if self.pressed[pygame.K_i]:
            return True
        return False

    def i_is_released(self):
        if self.released[pygame.K_i]:
            return True
        return False
    def j_is_pressed(self):
        if self.pressed[pygame.K_j]:
            return True
        return False

    def j_is_released(self):
        if self.released[pygame.K_j]:
            return True
        return False
    def k_is_pressed(self):
        if self.pressed[pygame.K_k]:
            return True
        return False

    def k_is_released(self):
        if self.released[pygame.K_k]:
            return True
        return False
    def l_is_pressed(self):
        if self.pressed[pygame.K_l]:
            return True
        return False

    def l_is_released(self):
        if self.released[pygame.K_l]:
            return True
        return False
    def m_is_pressed(self):
        if self.pressed[pygame.K_m]:
            return True
        return False

    def m_is_released(self):
        if self.released[pygame.K_m]:
            return True
        return False
    def n_is_pressed(self):
        if self.pressed[pygame.K_n]:
            return True
        return False

    def n_is_released(self):
        if self.released[pygame.K_n]:
            return True
        return False
    def o_is_pressed(self):
        if self.pressed[pygame.K_o]:
            return True
        return False

    def o_is_released(self):
        if self.released[pygame.K_o]:
            return True
        return False
    def p_is_pressed(self):
        if self.pressed[pygame.K_p]:
            return True
        return False

    def p_is_released(self):
        if self.released[pygame.K_p]:
            return True
        return False
    def q_is_pressed(self):
        if self.pressed[pygame.K_q]:
            return True
        return False

    def q_is_released(self):
        if self.released[pygame.K_q]:
            return True
        return False
    def r_is_pressed(self):
        if self.pressed[pygame.K_r]:
            return True
        return False

    def r_is_released(self):
        if self.released[pygame.K_r]:
            return True
        return False
    def s_is_pressed(self):
        if self.pressed[pygame.K_s]:
            return True
        return False

    def s_is_released(self):
        if self.released[pygame.K_s]:
            return True
        return False
    def t_is_pressed(self):
        if self.pressed[pygame.K_t]:
            return True
        return False

    def t_is_released(self):
        if self.released[pygame.K_t]:
            return True
        return False

    def u_is_pressed(self):
        if self.pressed[pygame.K_u]:
            return True
        return False

    def u_is_released(self):
        if self.released[pygame.K_u]:
            return True
        return False
    def v_is_pressed(self):
        if self.pressed[pygame.K_v]:
            return True
        return False

    def v_is_released(self):
        if self.released[pygame.K_v]:
            return True
        return False

    def w_is_pressed(self):
        if self.pressed[pygame.K_w]:
            return True
        return False

    def w_is_released(self):
        if self.released[pygame.K_w]:
            return True
        return False

    def x_is_pressed(self):
        if self.pressed[pygame.K_x]:
            return True
        return False

    def x_is_released(self):
        if self.released[pygame.K_x]:
            return True
        return False

    def y_is_pressed(self):
        if self.pressed[pygame.K_y]:
            return True
        return False

    def y_is_released(self):
        if self.released[pygame.K_y]:
            return True
        return False

    def z_is_pressed(self):
        if self.pressed[pygame.K_z]:
            return True
        return False

    def z_is_released(self):
        if self.released[pygame.K_z]:
            return True
        return False

    def left_is_pressed(self):
        if self.pressed[pygame.K_LEFT]:
            return True
        return False

    def left_is_released(self):
        if self.released[pygame.K_LEFT]:
            return True
        return False

    def right_is_pressed(self):
        if self.pressed[pygame.K_RIGHT]:
            return True
        return False

    def right_is_released(self):
        if self.released[pygame.K_RIGHT]:
            return True
        return False

    def down_is_pressed(self):
        if self.pressed[pygame.K_DOWN]:
            return True
        return False

    def down_is_released(self):
        if self.released[pygame.K_DOWN]:
            return True
        return False

    def up_is_pressed(self):
        if self.pressed[pygame.K_UP]:
            return True
        return False

    def up_is_released(self):
        if self.released[pygame.K_UP]:
            return True
        return False

    def tab_is_pressed(self):
        if self.pressed[pygame.K_TAB]:
            return True
        return False

    def tab_is_released(self):
        if self.released[pygame.K_TAB]:
            return True
        return False
