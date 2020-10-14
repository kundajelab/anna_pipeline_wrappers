import sys
task_file=sys.argv[1]
template_json=sys.argv[2]
out_dir=sys.argv[3] 
import json
tasks=open(task_file,'r').read().strip().split('\n')
for task in tasks:
    base=task.replace('.tagAlign.gz','').split('/')[-1]
    template=json.load(open(template_json,'r'))
    template['atac.tas'][0]=task
    with open(out_dir+'/'+base+'.json', 'w') as outfile:
        json.dump(template, outfile)
    
