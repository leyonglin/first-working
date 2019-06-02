#!/usr/bin/bash
/opt/apps/mysql/bin/mysql -udba_arch_table -pPUrKKChlZZqk@5436mHVCDOka -hlocalhost -S /opt/data/data_16303/mysql.sock -e "use gameplat_sc_data; call proc_insert_del_arch('gameplat_sc_data','live_pt_bet_record',1,'add_time');"

