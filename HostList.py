__author__ = 'alberto.sierra'

import qb

def hostlist():

    # Introducimos los IDs de los JOBs. No es necesario que haya Preview
    print 'No es necesario que haya PREVIEW\n'
    previewID = raw_input('Inserta el ID del Preview:\t')
    renderID = raw_input('Inserta el ID del Render:\t')

    job_subjobs = qb.jobinfo(fields=['subjobs'], id=[previewID,renderID])
    job_agenda = qb.jobinfo(fields=['agenda'], id=[previewID,renderID])
    job_render_subjobs = job_subjobs[0]
    job_render_agenda = job_agenda[0]['agenda']

    if previewID:
        job_preview_subjobs = job_subjobs[0]
        job_render_subjobs = job_subjobs[1]
        job_preview_agenda = job_agenda[0]['agenda']
        job_render_agenda = job_agenda[1]['agenda']
        job_agenda = job_preview_agenda + job_render_agenda
    else:
        job_agenda = job_render_agenda

    job_agenda_temp = {}

    #Creacion de un archivo de texto
    hosttext = open("T:\\renderfarm\\amp\\Documents\\HostList\\" + renderID + "_Hostlist.txt", 'w')

    # Recorre los frames del JOB, te muestra en pantalla y te lo copia al archivo de texto
    for frame in xrange(len(job_agenda)):
        #print job_agenda[frame]['name'], job_agenda[frame]['host']
        hosttext.write(job_agenda[frame]['name'] + ' ' + job_agenda[frame]['host'] + '\n')

hostlist()



