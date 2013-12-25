#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Bc Rx Recorded
# Generated: Wed Dec 25 12:59:04 2013
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class bc_rx_recorded(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Bc Rx Recorded")
		_icon_path = "/home/risu/.local/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/risu/Desktop/FCD_BC_RX/fcd_capture_sample.raw", True)
		self.blks2_wfm_rcv_0 = blks2.wfm_rcv(
			quad_rate=192000,
			audio_decimation=4,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.blocks_file_source_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.blks2_wfm_rcv_0, 0), (self.audio_sink_0, 0))
		self.connect((self.blocks_file_source_0, 0), (self.blks2_wfm_rcv_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = bc_rx_recorded()
	tb.Run(True)

