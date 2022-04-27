from .io import IO


_MAIN_BANNER = r"""{} 𝓑𝓲𝓵𝓑𝓞 𝓑𝓐𝓖𝓖𝓘𝓝𝓢 𝓡𝓔𝓥𝓔𝓝𝓖𝓔 𝓣𝓞𝓞𝓛

                {}by Hacker AnonJ  ~  
                                    v[_V_]

""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.Style.BRIGHT)


def get_main_banner(version):
    return _MAIN_BANNER.replace('[_V_]', version)
