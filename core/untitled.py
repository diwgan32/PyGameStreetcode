    def left_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not prior_key_states[pygame.K_LEFT]:
            return True
        return False

    def right_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not prior_key_states[pygame.K_RIGHT]:
            return True
        return False

    def up_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not prior_key_states[pygame.K_UP]:
            return True
        return False

    def down_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and not prior_key_states[pygame.K_DOWN]:
            return True
        return False

    def space_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not prior_key_states[pygame.K_SPACE]:
            return True
        return False

    def enter_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and not prior_key_states[pygame.K_ENTER]:
            return True
        return False

    def w_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not prior_key_states[pygame.K_w]:
            return True
        return False

    def a_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not prior_key_states[pygame.K_a]:
            return True
        return False

    def s_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and not prior_key_states[pygame.K_s]:
            return True
        return False

    def d_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not prior_key_states[pygame.K_d]:
            return True
        return False

    def shift_is_down(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RSHIFT] and not prior_key_states[pygame.K_RSHIFT]) or (keys[pygame.K_LSHIFT] and not prior_key_states[pygame.LSHIFT]):
            return True
        return False

    def tab_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB] and not prior_key_states[pygame.K_tab]:
            return True
        return False

    def q_is_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and not prior_key_states[pygame.K_q]:
            return True
        return False


    def e_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def r_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] and not prior_key_states[pygame.K_r]:
            return True
        return False

    def t_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t] and not prior_key_states[pygame.K_t]:
            return True
        return False

    def y_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y] and not prior_key_states[pygame.K_y]:
            return True
        return False

    def u_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_u] and not prior_key_states[pygame.K_u]:
            return True
        return False

    def i_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i] and not prior_key_states[pygame.K_i]:
            return True
        return False

    def o_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o] and not prior_key_states[pygame.K_o]:
            return True
        return False

    def p_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def f_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def g_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_g] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def h_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_h] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def j_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def k_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def l_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def z_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def x_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def c_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def v_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_v] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def b_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def n_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def m_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False

    def j_is_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e] and not prior_key_states[pygame.K_e]:
            return True
        return False