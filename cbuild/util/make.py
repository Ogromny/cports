_jobs = 1

def set_jobs(nj):
    global _jobs
    _jobs = nj

def jobs():
    return _jobs

class Make:
    def __init__(self, tmpl, jobs = None, command = None, env = {}):
        self.template = tmpl
        self.command = command if command else tmpl.make_cmd
        self.env = env
        if not jobs:
            self.jobs = _jobs
        else:
            self.jobs = jobs

    def invoke(self, targets = [], args = [], jobs = None, env = {}):
        renv = dict(self.env)
        renv.update(env)

        if not jobs:
            jobs = self.jobs

        if self.template.disable_parallel_build:
            jobs = 1

        argsbase = ["-j" + str(jobs)]

        if targets:
            if isinstance(targets, list):
                argsbase += targets
            else:
                argsbase.append(str(targets))

        argsbase += args

        return self.template.do(
            self.command, argsbase, build = True, env = renv
        )

    def build(self, args = [], jobs = None, env = {}):
        pkg = self.template
        return self.invoke(
            pkg.make_build_target, pkg.make_build_args + args, jobs, env
        )

    def install(self, args = [], jobs = None, env = {}, default_args = True):
        pkg = self.template
        argsbase = []

        if default_args:
            argsbase.append("DESTDIR=" + str(pkg.chroot_destdir))

        argsbase += pkg.make_install_args
        argsbase += args

        return self.invoke(pkg.make_install_target, argsbase, jobs, env)
