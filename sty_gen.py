
_PACKAGE_INC_TEMPLATE=r"""\@ifpackageloaded{#P_INC}{% already included
\PackageInfo{#P_CUR}{Package #P_INC was already included}
}
{% not included
\RequirePackage{#P_INC}
}"""
_PACKAGE_INC_W_O_TEMPLATE=r"""\@ifpackageloaded{#P_INC}{% already included
\PackageInfo{#P_CUR}{Package #P_INC was already included}
}
{% not included
\RequirePackage[#P_OPT]{#P_INC}
}"""


def gen_package_includes(packages, sty='lecture'):
    """

    Args:
        packages:  list of str, packages to be included
        sty:       str, current sty

    Returns:

    """
    _PACKAGE_INC_TEMPLATE_ = _PACKAGE_INC_TEMPLATE.replace('#P_CUR', sty)
    _PACKAGE_INC_W_O_TEMPLATE_ = _PACKAGE_INC_W_O_TEMPLATE.replace('#P_CUR', sty)

    content = []
    for p in packages:
        package = p.split(':')
        if len(package) > 1:
            content.append(
                _PACKAGE_INC_W_O_TEMPLATE_.replace(
                    '#P_INC', package[0]
                ).replace('#P_OPT', package[1]))
        else:
            content.append(
                _PACKAGE_INC_TEMPLATE_.replace(
                    '#P_INC', package[0]
                )
            )
    return '\n\n'.join(content)


if __name__ == '__main__':
    with open('packages_for_lecture_sty.txt', 'r') as fp:
        packages = [line.strip() for line in fp.readlines()]

        print gen_package_includes(packages)

