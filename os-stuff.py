import os
from collections import OrderedDict
def path_tree(base='.',path='.',excludes=None):
    os.chdir(base)
    os.path.abspath('.')

    excluded_paths = set()
    if excludes:
        for p in excludes:
            excluded_paths.add(p)
        print('excluded_paths=',excluded_paths)
    def paths(level=0,path=None):
        _dirs = OrderedDict()
        _fils = OrderedDict()
        for f in os.listdir(path=path):
            pf = path + os.sep + f
            if os.path.isdir(pf):
                if f not in excluded_paths:
                    _dirs[f]=1
                    yield ( level, pf )
                    yield from paths(level=level+1, path=pf)
            else:
                if f not in excluded_paths:
                    _fils[f]=1
    for depth,f in paths(path=path):
        print(' '*depth, f, os.path.basename(f))
        print()
if __name__ == '__main__':
    from   sys import argv
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-b','--base',dest='base_path',default='..',help='base path')
    parser.add_argument('-w','--walk',dest='walker_path',default='..',help='walk ')
    parser.add_argument('-x', '--exclude', dest='excluded_folders', default=['.git'], nargs='*', help='folder to exclude')
    args=parser.parse_args(argv[1:])
    if args.walker_path:
        path_tree(path=args.walker_path,excludes=args.excluded_folders,base=args.base_path)
