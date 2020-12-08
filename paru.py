import os
import subprocess
import dotbot

class Paru(dotbot.Plugin):
  def can_handle(self, directive):
    return directive in ['pacman', 'paru']

  def handle(self, directive, data):
    if not self.can_handle(directive):
      self._log.error('dotbot-paru cannot handle directive {}'.format(directive))
      return False
    if self._bootstrap() != 0:
      self._log.error('Paru is not installed on your system, and bootstrapping failed')
      return False
    return self._install(data)

  def _install(self, packages):
    package_list = ' '.join(packages)
    cmd = 'paru --needed --noconfirm -Syu -- {}'.format(package_list)

    self._log.info('Installing {}'.format(package_list))
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

    if result.returncode == 0:
      self._log.info('All packages installed successfully')
    else:
      self._log.error('Some packages failed to install')
    return result.returncode == 0

  def _bootstrap(self):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cmd = '{}/bootstrap'.format(dir_path)
    return subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True).returncode
