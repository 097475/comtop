import os
import numpy as np

import pyedflib
from stacklineplot import stackplot

#TODO: memory leaks
def test():
    f = pyedflib.data.test_generator()
    print("\nlibrary version: %s" % pyedflib.version.version)

    print("\ngeneral header:\n")

    # print("filetype: %i\n"%hdr.filetype);
    print("edfsignals: %i" % f.signals_in_file)
    print("file duration: %i seconds" % f.file_duration)
    print("startdate: %i-%i-%i" % (f.getStartdatetime().day,f.getStartdatetime().month,f.getStartdatetime().year))
    print("starttime: %i:%02i:%02i" % (f.getStartdatetime().hour,f.getStartdatetime().minute,f.getStartdatetime().second))
    # print("patient: %s" % f.getP);
    # print("recording: %s" % f.getPatientAdditional())
    print("patientcode: %s" % f.getPatientCode())
    print("gender: %s" % f.getGender())
    print("birthdate: %s" % f.getBirthdate())
    print("patient_name: %s" % f.getPatientName())
    print("patient_additional: %s" % f.getPatientAdditional())
    print("admincode: %s" % f.getAdmincode())
    print("technician: %s" % f.getTechnician())
    print("equipment: %s" % f.getEquipment())
    print("recording_additional: %s" % f.getRecordingAdditional())
    print("datarecord duration: %f seconds" % f.getFileDuration())
    print("number of datarecords in the file: %i" % f.datarecords_in_file)
    print("number of annotations in the file: %i" % f.annotations_in_file)

    channel = 7
    print("\nsignal parameters for the %d.channel:\n\n" % channel)

    print("label: %s" % f.getLabel(channel))
    print("samples in file: %i" % f.getNSamples()[channel])
    # print("samples in datarecord: %i" % f.get
    print("physical maximum: %f" % f.getPhysicalMaximum(channel))
    print("physical minimum: %f" % f.getPhysicalMinimum(channel))
    print("digital maximum: %i" % f.getDigitalMaximum(channel))
    print("digital minimum: %i" % f.getDigitalMinimum(channel))
    print("physical dimension: %s" % f.getPhysicalDimension(channel))
    print("prefilter: %s" % f.getPrefilter(channel))
    print("transducer: %s" % f.getTransducer(channel))
    print("samplefrequency: %f" % f.getSampleFrequency(channel))

    annotations = f.readAnnotations()
    for n in np.arange(f.annotations_in_file):
        print("annotation: onset is %f    duration is %s    description is %s" % (annotations[0][n],annotations[1][n],annotations[2][n]))

    buf = f.readSignal(channel)
    n = 200
    print("\nread %i samples\n" % n)
    result = ""
    for i in np.arange(n):
        result += ("%.1f, " % buf[i])
    print(result)
    f._close()
    del f

def readEDF(path):
    return pyedflib.EdfReader(path)


def edfToMatrix(data):
    height = data.signals_in_file
    ret = []
    for i in range(height):
        ret.append(data.readSignal(i))
    return np.array(ret)

def plotEDF(data):##TODO dati si cancellano dopo plotting
    n = data.signals_in_file
    signal_labels = data.getSignalLabels()
    n_min = data.getNSamples()[0]
    sigbufs = [np.zeros(data.getNSamples()[i]) for i in np.arange(n)]
    for i in np.arange(n):
        sigbufs[i] = data.readSignal(i)
        if n_min < len(sigbufs[i]):
            n_min = len(sigbufs[i])
    #data._close()

    n_plot = np.min((n_min, 2000))
    sigbufs_plot = np.zeros((n, n_plot))
    for i in np.arange(n):
        sigbufs_plot[i,:] = sigbufs[i][:n_plot]

    stackplot(sigbufs_plot[:, :n_plot], ylabels=signal_labels)

if __name__ == '__main__':
    '''
    r = edfToMatrix(pyedflib.data.test_generator())
    print(len(r))
    print(len(r[0]))
    print(len(r[1]))
    print(type(r))
    print(type(r[0]))
    plotEDF(pyedflib.data.test_generator())
    '''
    a = readEDF('prova.edf')
    plotEDF(a)
    print(edfToMatrix(a))

   