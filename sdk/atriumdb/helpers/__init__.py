# AtriumDB is a timeseries database software designed to best handle the unique features and
# challenges that arise from clinical waveform data.
#     Copyright (C) 2023  The Hospital for Sick Children
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from importlib import resources
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


_cfg = tomllib.loads(resources.read_text("atriumdb.helpers", "config.toml"))
_shared_lib_linux_name = _cfg["resources"]["shared_lib_filename_linux"].split("/")[-1]
_shared_lib_windows_name = _cfg["resources"]["shared_lib_filename_windows"].split("/")[-1]

def get_shared_lib_path(platform: str):
    if platform == "win32":
        return resources.files("atriumdb.bin").joinpath(_shared_lib_windows_name)
    else:
        return resources.files("atriumdb.bin").joinpath(_shared_lib_linux_name)

protected_mode_default_setting = _cfg["settings"]["protected_mode"]
overwrite_default_setting = _cfg["settings"]["overwrite"]
protected_mode_default_setting = _cfg["settings"]["protected_mode"]
overwrite_default_setting = _cfg["settings"]["overwrite"]
