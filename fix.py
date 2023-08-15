import os
import glob
from pprint import pprint
import shutil


def delete_folder(f):
    print("Delete here")
    shutil.rmtree(f)

def copy_file(f, nloc):
    if not os.path.exists(nloc):
        os.mkdir(nloc)
    fp = f.split("/")
    fn = fp[len(fp)-1]
    new_name = nloc + fn
    os.rename(f, new_name)
    print("copied from {0} to {1}".format(f, new_name))

def copy_files(files, nloc):
    for f in files:
        copy_file(f, nloc)

def dig_in_folder(folder):
    all_files = []
    subfolders = [f.path for f in os.scandir(folder) if f.is_dir() ]
    if len(subfolders) > 0:
        for f in subfolders:
            subf = dig_in_folder(f)
            all_files += subf

    for file in os.listdir(folder):
        if file.endswith(".wav") or file.endswith(".mp3"):
            fn = folder + '/' + str(file)
            all_files.append(fn)

    proc = []
    for i, nf in enumerate(all_files):
        if nf[0] != '/':
            o = all_files[i-1] + nf
            proc.append(o)
        else:
            if nf[-3:] == 'wav' or nf[-3:] == 'mp3':
                proc.append(nf)



    return proc

def copy_to_triage(folder, triage_folder):
    subfolders = [f.path for f in os.scandir(folder) if f.is_dir() ]
    for f in subfolders:
        files = dig_in_folder(f)

        copy_files(files, triage_folder)
        delete_folder(f)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_note(txt):
    notes = ['a', 'bb', 'c', 'db', 'd', 'e', 'eb', 'f', 'f', 'fb']
    if txt in notes:
        return True
    else:
        return False

def cleanup_triage(triage, parent, map):
    ll = len(os.listdir(triage))
    for file in os.listdir(triage):
        if file.endswith(".wav") or file.endswith(".mp3"):
            fn = file.lower()
            ol = triage + file
            found = False
            if 'loop' in fn:
                if 'loops' in map:
                    nd = parent + map['loops']
                    copy_file(ol, nd)
            else:
                if 'kick' in fn and 'kicks' in map:
                    nd = parent + map['kicks']
                    copy_file(ol, nd)


                elif ('snare' in fn or 'snr' in fn) and 'snares' in map:
                    nd = parent + map['snares']
                    copy_file(ol, nd)

                elif ('clap' in fn or 'snap' in fn or 'clp' in fn) and 'claps' in map:
                    nd = parent + map['claps']
                    copy_file(ol, nd)

                elif ('hat' in fn or 'hh' in fn) and 'hats' in map:
                    nd = parent + map['hats']
                    copy_file(ol, nd)

                elif '808' in fn and '808s' in map:
                    nd = parent + map['808s']
                    copy_file(ol, nd)

                else:

                    if 'cymbals' in map:
                        if 'crash' in fn or 'ride' in fn or 'splash' in fn or 'cymbal' in fn:
                            nd = parent + map['cymbals']
                            copy_file(ol, nd)
                            found = True
                    if 'perc' in map:
                        if 'percussion' in fn or 'bongo' in fn or 'conga' in fn or 'perc' in fn or 'tom' in fn or 'prc' in fn or 'shaker' in fn or 'rim' in fn or 'bell' in fn:
                            nd = parent + map['perc']
                            copy_file(ol, nd)
                            found = True

                    # if 'vocals' in map and not found:
                    #     if 'vox' in fn or 'vocal' in fn or 'choir' in fn:
                    #         nd = parent + map['vocals']
                    #         copy_file(ol, nd)
                    #         found = True


                    if 'one shots' in map and not found:
                        if 'synth' in fn or 'vocal' in fn or 'bass' in fn or 'one shot' in fn or ('one' in fn and 'shot' in fn) or 'keys' in fn or 'sax' in fn or 'chord' in fn or 'strum' in fn or 'note' in fn or 'brass' in fn:
                            nd = parent + map['one shots']
                            copy_file(ol, nd)
                            found = True


                    if 'fx' in map and not found:
                        if 'fx' in fn or 'sweep' in fn or 'texture' in fn or 'bend' in fn or 'ambiance' in fn or 'ambience' in fn:
                            nd = parent + map['fx']
                            copy_file(ol, nd)


                    if not found:
                        fp = fn.split("_")
                        for p in fp:
                            if is_note(p) and not found:
                                if 'one shots' in map:
                                    nd = parent + map['one shots']
                                    copy_file(ol, nd)
                                    found = True

                            if is_number(p) and not found:
                                if int(p) > 60 and 'loops' in map:
                                    nd = parent + map['loops']
                                    copy_file(ol, nd)
                                    found = True



mess_folder = "/Users/kevindenny/Splice/sounds/packs/"

triage_folder = '/Users/kevindenny/hdmi fx Dropbox/Kevin Denny/drums/sample triage/'

new_parent_folder = '/Users/kevindenny/hdmi fx Dropbox/Kevin Denny/drums/'

sub_dirs_map = {
    'hats': 'hats/',
    'loops': 'loops from splice/',
    'one shots': 'melod one shots/',
    'perc': 'perc/',
    'snares': 'snares/',
    '808s': '808s/',
    'claps': 'claps/',
    'fx': 'fx/',
    'kicks': 'kicks/',
    'cymbals': 'cymbals/',
    'vocals': 'vocals/'
}

copy_to_triage(mess_folder, triage_folder)


cleanup_triage(triage_folder, new_parent_folder, sub_dirs_map)