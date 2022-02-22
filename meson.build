project('seamlesscontrol',
          version: '0.1.0',
    meson_version: '>= 0.50.0',
  default_options: [ 'warning_level=2',
                   ],
)

i18n = import('i18n')



subdir('data')
subdir('src')
subdir('po')
install_subdir('systemd', install_dir: '/usr/lib/systemd/user/')

meson.add_install_script('build-aux/meson/postinstall.py')
