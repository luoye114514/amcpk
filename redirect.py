# file: ./extracted\0_8d7bfdc9.pyc
# cracked by asJony


def init_rotor():
    asdf_dn = 'j2h56ogodh3sk'
    asdf_dt = '=dziaq;'
    asdf_df = '|`o=5v7!"-276'
    asdf_tm = asdf_dn * 4 + (asdf_dt + asdf_dn + asdf_df) * 5 + '$' + '@' + asdf_dt * 7 + asdf_df * 2 + '&' + ']' + '`'
    import rotor
    return rotor.newrotor(asdf_tm)


class McpImporter(object):
    rot = init_rotor()
    Ext = '.mcs'

    def __init__(self, path):
        self._path = path

    def find_module(self, fullname, path = None):
        import fop
        if path is None:
            path = self._path
        fullname = fullname.replace('.', '/')
        pkg_name = ''.join((fullname, '/__init__', McpImporter.Ext))
        if fop.find_file(pkg_name, path):
            return self
        else:
            fullname += McpImporter.Ext
            if fop.find_file(fullname, path):
                return self
            return

    def load_module(self, fullname):
        import fop, marshal, zlib
        is_pkg = True
        mod_path = fullname.replace('.', '/') + '/__init__'
        mod_name = fullname
        if not fop.find_file(mod_path + McpImporter.Ext, self._path):
            is_pkg = False
            mod_path = fullname.replace('.', '/')
            mod_name = fullname
        data = fop.get_file(mod_path + McpImporter.Ext, self._path)
        data = McpImporter.rot.decrypt(data)
        data = zlib.decompress(data)
        data = self._reverse_data(data)
        code = marshal.loads(data)
        path = None
        if is_pkg:
            path = [self._path]
        return fop.new_module(mod_name, code, path)

    def read_module(self, fullname, data):
        import fop, marshal, zlib
        data = McpImporter.rot.decrypt(data)
        data = zlib.decompress(data)
        data = self._reverse_data(data)
        code = marshal.loads(data)
        return fop.new_module(fullname, code, None)

    def _reverse_data(self, data):
        L = list(data)
        L = map(lambda ch: chr(ord(ch) ^ 156), L[:130]) + L[130:]
        L.reverse()
        return ''.join(L)


import sys
del sys.path_hooks[:]
sys.path_hooks.append(McpImporter)
sys.path_importer_cache.clear()
