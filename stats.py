import objc_dep
import subprocess

git_path = '/Users/cmccarty/code/tripadvisor/mobile/ta-ios-mobile'
project_path = git_path + '/Code/Models'



def run_stats():
    (d, d2) = objc_dep.generate_dependencies(project_path, None, None, None, None)
    print objc_dep.get_dependency_stats(d)
    print objc_dep.get_dependency_stats(d2)
    print '-------------------'
    
def get_commits():
    d = git_path + '/.git'
    cmd = '/usr/local/bin/git --git-dir=%s log --pretty="format:%%H"' % (d)
    output = run_command(cmd)    
    commits = output.split('\n')

    return ['34030022afe533d3c38bc7082fca7974975db06c']
    return commits[-10:]


def checkout_commit(commit):
    d = git_path + '/.git'
    cmd = 'git --git-dir=%s checkout --quiet %s' % (d, commit)
    o = run_command(cmd)
    return

def run_status_for_commit(commit):
    # check out commit
    checkout_commit(commit)
    
    # run stats for current checkout 
    stats = run_stats()
    return stats   

def run_command(command):
    print command
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).communicate()
    return p[0]
   


def main():
    commits = get_commits()
    if not commits:
        print 'No commits found'
        return
    
    for c in commits:
        stats = run_status_for_commit(c)
        print stats
        
        
        
        
        
if __name__ == '__main__':
    main()





