import datetime
import os
import time

import matplotlib
from Chan import CChan
from ChanConfig import CChanConfig
from Common.CEnum import AUTYPE, DATA_SRC, KL_TYPE
from Plot.AnimatePlotDriver import CAnimateDriver
from Plot.PlotDriver import CPlotDriver


def draw_single_stock(s,count, begin_time, end_time, data_src, lv_list, config, plot_config, plot_para):
    endtime = datetime.datetime.strptime(end_time, "%Y-%m-%d")
    endtime = endtime - datetime.timedelta(days=count)
    for i in range(count):
        endtime1 = endtime + datetime.timedelta(days=i)
        if endtime1.weekday() == 5 or endtime1.weekday() == 6:
            continue
        end_time1 = endtime1.strftime("%Y-%m-%d")
        try:
            chan = CChan(
                code=s,
                begin_time=begin_time,
                end_time=end_time1,
                data_src=data_src,
                lv_list=lv_list,
                config=config,
                autype=AUTYPE.QFQ,
            )
            counter=0
            for _ in chan.step_load():
                counter+=1
                if counter<262:continue
                #jj = chan.toJson()
                if not os.path.exists(f"./bs/{s}"):
                    os.makedirs(f"./bs/{s}")
                if config.trigger_step:
                    plot_driver = CPlotDriver(
                        chan,
                        plot_config=plot_config,
                        plot_para=plot_para,
                    )
                    #plot_driver.figure.show()

                    plot_driver.save2img(f"./bs/{s}/{s}_{counter}.png")
                    matplotlib.pyplot.close()
                else:
                    CAnimateDriver(
                        chan,
                        plot_config=plot_config,
                        plot_para=plot_para,
                    )
        except Exception as e:
            print(e)
        i += 1
        print(i,s)
        #time.sleep(3)


if __name__ == "__main__":
    code = "sh.688090"
    begin_time = "2024-01-01"
    end_time = "2024-12-11"
    data_src = DATA_SRC.BAO_STOCK
    lv_list = [KL_TYPE.K_30M]

    config = CChanConfig({
        "bi_strict": True,
        "trigger_step": True,
        "skip_step": 0,
        "divergence_rate": float("inf"),
        "bsp2_follow_1": False,
        "bsp3_follow_1": False,
        "min_zs_cnt": 0,
        "bs1_peak": False,
        "macd_algo": "peak",
        "bs_type": '1,2,3a,1p,2s,3b',
        "print_warning": True,
        "zs_algo": "normal",
    })

    plot_config = {
        "plot_kline": True,
        "plot_kline_combine": True,
        "plot_bi": True,
        "plot_seg": True,
        "plot_eigen": False,
        "plot_zs": True,
        "plot_macd": False,
        "plot_mean": False,
        "plot_channel": False,
        "plot_bsp": True,
        "plot_extrainfo": False,
        "plot_demark": False,
        "plot_marker": False,
        "plot_rsi": False,
        "plot_kdj": False,
    }

    plot_para = {
        "seg": {
            # "plot_trendline": True,
        },
        "bi": {
            # "show_num": True,
            # "disp_end": True,
        },
        "figure": {
            "x_range": 200,
        },
        "marker": {
            # "markers": {  # text, position, color
            #     '2023/06/01': ('marker here', 'up', 'red'),
            #     '2023/06/08': ('marker here', 'down')
            # },
        }
    }
    i=0
    skip=True
    sl =['000722.SZ', '603890.SH', '300729.SZ', '002376.SZ', '000417.SZ', '603889.SH', '002838.SZ', '601008.SH', '600495.SH', '603703.SH', '601188.SH', '603969.SH', '600318.SH', '000551.SZ', '600830.SH', '000823.SZ', '603038.SH', '600301.SH', '300790.SZ', '600101.SH', '603111.SH', '600593.SH', '603088.SH', '300814.SZ', '300326.SZ', '002881.SZ', '605016.SH', '002134.SZ', '603166.SH', '603015.SH', '605286.SH', '301291.SZ', '300847.SZ', '300320.SZ', '002970.SZ', '002111.SZ', '605056.SH', '600713.SH', '600103.SH', '603897.SH', '300953.SZ', '000045.SZ', '002947.SZ', '002119.SZ', '600468.SH', '603929.SH', '603439.SH', '603408.SH', '300975.SZ', '301058.SZ', '603112.SH', '002570.SZ', '300926.SZ', '002438.SZ', '300781.SZ', '300067.SZ', '605305.SH', '603031.SH', '600361.SH', '000534.SZ', '002124.SZ', '002014.SZ', '002096.SZ', '300507.SZ', '605196.SH', '600897.SH', '002284.SZ', '300292.SZ', '603301.SH', '603060.SH', '002707.SZ', '601116.SH', '002766.SZ', '605507.SH', '300183.SZ', '300201.SZ', '600817.SH', '600770.SH', '002536.SZ', '600368.SH', '300143.SZ', '301297.SZ', '300307.SZ', '300825.SZ', '002440.SZ', '002880.SZ', '002533.SZ', '601886.SH', '000886.SZ', '300232.SZ', '600961.SH', '003013.SZ', '000968.SZ', '600496.SH', '300711.SZ', '300815.SZ', '603855.SH', '000936.SZ', '002102.SZ', '002590.SZ', '300820.SZ', '000524.SZ', '600268.SH', '002961.SZ', '002194.SZ', '301000.SZ', '603995.SH', '600162.SH', '000900.SZ', '600979.SH', '300581.SZ', '300151.SZ', '002649.SZ', '300913.SZ', '603680.SH', '001309.SZ', '002208.SZ', '000962.SZ', '603181.SH', '002897.SZ', '605183.SH', '000957.SZ', '603368.SH', '300470.SZ', '002703.SZ', '600987.SH', '600861.SH', '600874.SH', '601226.SH', '600531.SH', '002175.SZ', '300493.SZ', '002892.SZ', '300822.SZ', '600751.SH', '603169.SH', '300968.SZ', '603499.SH', '301293.SZ', '600226.SH', '300602.SZ', '300304.SZ', '002023.SZ', '300482.SZ', '300342.SZ', '002275.SZ', '300401.SZ', '300768.SZ', '301301.SZ', '601619.SH', '600618.SH', '300925.SZ', '603809.SH', '301219.SZ', '000821.SZ', '300131.SZ', '600366.SH', '300360.SZ', '300870.SZ', '300113.SZ', '605376.SH', '300079.SZ', '603588.SH', '002093.SZ', '002073.SZ', '002997.SZ', '002534.SZ', '603508.SH', '000899.SZ', '300527.SZ', '002378.SZ', '002043.SZ', '000885.SZ', '002351.SZ', '002545.SZ', '603713.SH', '603053.SH', '300327.SZ', '300035.SZ', '300049.SZ', '300783.SZ', '300046.SZ', '600305.SH', '603693.SH', '605198.SH', '300303.SZ', '002267.SZ', '002967.SZ', '300398.SZ', '002987.SZ', '002901.SZ', '000048.SZ', '300705.SZ', '002891.SZ', '600882.SH', '002020.SZ', '002434.SZ', '603698.SH', '300638.SZ', '300415.SZ', '000791.SZ', '601528.SH', '600509.SH', '300181.SZ', '300685.SZ', '600917.SH', '002626.SZ', '601609.SH', '300917.SZ', '600664.SH', '000950.SZ', '601311.SH', '603881.SH', '301004.SZ', '300772.SZ', '002396.SZ', '001286.SZ', '603690.SH', '300319.SZ', '600017.SH', '300821.SZ', '600186.SH', '300618.SZ', '002488.SZ', '300170.SZ', '002204.SZ', '603919.SH', '603530.SH', '603055.SH', '002249.SZ', '600458.SH', '001287.SZ', '603583.SH', '002315.SZ', '002928.SZ', '600114.SH', '003006.SZ', '001301.SZ', '300236.SZ', '300357.SZ', '300492.SZ', '603083.SH', '002061.SZ', '300811.SZ', '300573.SZ', '300184.SZ', '600821.SH', '600163.SH', '301050.SZ', '300613.SZ', '300620.SZ', '300634.SZ', '600993.SH', '600995.SH', '600292.SH', '600648.SH', '300777.SZ', '300083.SZ', '601136.SH', '301171.SZ', '600728.SH', '002948.SZ', '301498.SZ', '300010.SZ', '300641.SZ', '002895.SZ', '002245.SZ', '002668.SZ', '600662.SH', '601020.SH', '600285.SH', '600572.SH', '603983.SH', '300276.SZ', '000969.SZ', '300972.SZ', '300570.SZ', '002755.SZ', '300761.SZ', '300100.SZ', '002831.SZ', '300827.SZ', '600718.SH', '002847.SZ', '000818.SZ', '002270.SZ', '603393.SH', '300677.SZ', '300475.SZ', '000550.SZ', '000680.SZ', '002597.SZ', '603218.SH', '603355.SH', '603888.SH', '603733.SH', '000966.SZ', '603171.SH', '002126.SZ', '601137.SH', '603039.SH', '600577.SH', '300133.SZ', '601126.SH', '603283.SH', '300567.SZ', '605111.SH', '600633.SH', '002221.SZ', '301015.SZ', '603337.SH', '603638.SH', '605333.SH', '600428.SH', '000902.SZ', '000682.SZ', '002911.SZ', '002468.SZ', '000403.SZ', '601222.SH', '300285.SZ', '601369.SH', '002139.SZ', '601156.SH', '000766.SZ', '002226.SZ', '600711.SH', '605296.SH', '002557.SZ', '603009.SH', '603296.SH', '002698.SZ', '002222.SZ', '300529.SZ', '603236.SH', '600933.SH', '300182.SZ', '603317.SH', '002400.SZ', '000967.SZ', '603766.SH', '600216.SH', '002402.SZ', '000688.SZ', '300666.SZ', '300487.SZ', '002266.SZ', '002507.SZ', '000528.SZ', '600928.SH', '301078.SZ', '600575.SH', '002906.SZ', '601702.SH', '603025.SH', '601963.SH', '000636.SZ', '002506.SZ', '600056.SH', '002984.SZ', '300454.SZ', '603005.SH', '003021.SZ', '002145.SZ', '002851.SZ', '603556.SH', '300627.SZ', '000039.SZ', '600872.SH', '601965.SH', '605589.SH', '002653.SZ', '002683.SZ', '600764.SH', '000537.SZ', '300458.SZ', '300724.SZ', '000683.SZ', '002044.SZ', '600559.SH', '603613.SH', '002409.SZ', '000686.SZ', '002461.SZ', '300054.SZ', '600685.SH', '300432.SZ', '300679.SZ', '002432.SZ', '002850.SZ', '603379.SH', '600062.SH', '300442.SZ', '002837.SZ', '300136.SZ', '300604.SZ', '600486.SH', '002155.SZ', '300763.SZ', '300115.SZ', '300558.SZ', '603129.SH', '603662.SH', '002120.SZ', '300751.SZ', '603179.SH', '000830.SZ', '002262.SZ', '300346.SZ', '002130.SZ', '002926.SZ', '002472.SZ', '601128.SH', '300002.SZ', '002065.SZ', '600004.SH', '300001.SZ', '603920.SH', '002138.SZ', '600316.SH', '002500.SZ', '603786.SH', '600143.SH', '600583.SH', '300857.SZ', '300373.SZ', '600578.SH', '601399.SH', '001696.SZ', '600021.SH', '600312.SH', '600141.SH', '603087.SH', '603979.SH', '601665.SH', '600598.SH', '000729.SZ', '601866.SH', '300866.SZ', '300623.SZ', '600521.SH', '600171.SH', '600563.SH', '002517.SZ', '600208.SH', '600998.SH', '000750.SZ', '601966.SH', '600378.SH', '603596.SH', '300628.SZ', '600988.SH', '600779.SH', '000738.SZ', '002608.SZ', '002273.SZ', '603939.SH', '300699.SZ', '601456.SH', '002602.SZ', '600299.SH', '600909.SH', '600901.SH']
    sl =['600560.SH']
    for s in sl:
        try:

            # if skip and s == "002111.SZ":
            #     skip = False
            # if skip:
            #     continue
            draw_single_stock(s,1, begin_time, end_time, data_src, lv_list, config, plot_config, plot_para)
        except Exception as e:
            print(e)
        i += 1
        print(i,s)
        time.sleep(3)

        if skip ==False:
            break
