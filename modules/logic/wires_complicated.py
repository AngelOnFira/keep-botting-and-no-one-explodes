# primary   attributes: colors
# secondary attributes: star, led
# ternary   attributes: 2+ batt, parallel, sn even

has_two_plus_batt   = lambda **kwargs : kwargs['two_plus_batt']
has_parallel        = lambda **kwargs : kwargs['parallel']
is_sn_even          = lambda **kwargs : kwargs['sn_even']
is_true             = lambda **kwargs : True
is_false            = lambda **kwargs : False

rules = {
  'white': {
    'none': is_true,
    'star': is_true,
    'led':  is_false,
    'both': has_two_plus_batt,
  },
  'red': {
    'none': is_sn_even,
    'star': is_true,
    'led':  has_two_plus_batt,
    'both': has_two_plus_batt,
  },
  'blue': {
    'none': is_sn_even,
    'star': is_false,
    'led':  has_parallel,
    'both': has_parallel,
  },
  'both': {
    'none': is_sn_even,
    'star': has_parallel,
    'led':  is_sn_even,
    'both': is_false,
  },
}

class WiresComplicated:

    def solution(self, colors, has_star, has_led, battery_count, has_parallel, serial_number):
        primary = colors[0] if len(colors) == 1 else 'both'
        
        if has_star and has_led:
            secondary = 'both'
        elif has_star and not has_led:
            secondary = 'star'
        elif not has_star and has_led:
            secondary = 'led'
        else:
            secondary = 'none'

        validator       = rules[primary][secondary]

        return validator(
            two_plus_batt=battery_count >= 2,
            parallel=has_parallel,
            sn_even=int(serial_number[-1:]) % 2 == 0)