import sys

import matplotlib as mpl
import matplotlib.pyplot as plt

def test_axes_default():
    # create plot with default
    fig, ax = plt.subplots()
    hlines = ax.hlines(0.5, 0, 1)
    vlines = ax.vlines(0.5, 0, 1)

    # check matches expected default
    hlines_passes = mpl.colors.same_color(hlines.get_color(), 'k')
    vlines_passes = mpl.colors.same_color(vlines.get_color(), 'k')

    # error out if not matching
    if not hlines_passes or not vlines_passes:
        print('Failed to pass axes interface default test')
        sys.exit()

def test_axes_rc_params():
        # create plot with rcParams defaults
        fig, ax = plt.subplots()

        with mpl.rc_context({'lines.color': 'blue'}):
            hlines = ax.hlines(0.5, 0, 1)
            vlines = ax.vlines(0.5, 0, 1)

            # check matches expected rcParams
            hlines_passes = mpl.colors.same_color(hlines.get_color(), mpl.rcParams['lines.color'])
            vlines_passes = mpl.colors.same_color(vlines.get_color(), mpl.rcParams['lines.color'])

            if not hlines_passes or not vlines_passes:
                print('Failed to pass axes interface rcParams test')
                sys.exit()

def test_pyplot():
    # create plot figure through pyplot interface
    plt.figure()

    with mpl.rc_context({'lines.color': 'blue'}):
        hlines = plt.hlines(0.5, 0, 1)
        vlines = plt.vlines(0.5, 0, 1, colors='k')

        # check matches expected rcParams
        hlines_passes = mpl.colors.same_color(hlines.get_color(), mpl.rcParams['lines.color'])
        vlines_passes = mpl.colors.same_color(vlines.get_color(), 'k')

        if not hlines_passes or not vlines_passes:
            print('Failed to pass pyplot interface test')
            sys.exit()

if __name__ == '__main__':
    # run tests
    test_axes_default()
    test_axes_rc_params()
    test_pyplot()
    # notify user of success
    print('Successfully passed User Acceptance testing!')
