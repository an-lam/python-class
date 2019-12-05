#############################################################################
# Generated by PAGE version 4.9
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font13
vTcl:font:add_font \
    "-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font14
vTcl:font:add_font \
    "-family {Segoe UI} -size 9 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font15
vTcl:font:add_font \
    "-family {Segoe UI Emoji} -size 10 -weight bold -slant italic -underline 1 -overstrike 0" \
    user \
    vTcl:font17
vTcl:font:add_font \
    "-family {Segoe UI Symbol} -size 11 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font18
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top50
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra51
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# USER DEFINED PROCEDURES
#

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top50 {base} {
    if {$base == ""} {
        set base .top50
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 523x371+443+146
    update
    # set in toplevel.wgt.
    global vTcl
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1354 733
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Devices Database"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra51 \
        -borderwidth 4 -relief groove -background {#8080ff} -height 355 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 505 
    vTcl:DefineAlias "$top.fra51" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra51
    entry $site_3_0.ent52 \
        -background {#c0c0c0} -borderwidth 4 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable ipp1 -validate key 
    vTcl:DefineAlias "$site_3_0.ent52" "ippart1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text . 
    vTcl:DefineAlias "$site_3_0.lab53" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent55 \
        -background {#c0c0c0} -borderwidth 4 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable ipp2 -validate key 
    vTcl:DefineAlias "$site_3_0.ent55" "ippart2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text . 
    vTcl:DefineAlias "$site_3_0.lab56" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent58 \
        -background {#c0c0c0} -borderwidth 4 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable ipp3 -validate key 
    vTcl:DefineAlias "$site_3_0.ent58" "ippart3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab59 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font14,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text . 
    vTcl:DefineAlias "$site_3_0.lab59" "Label3" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent60 \
        -background {#c0c0c0} -borderwidth 4 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable ipp4 -validate key 
    vTcl:DefineAlias "$site_3_0.ent60" "ippart4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but61 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 4 -command callback_add \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font15,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text {Add New} 
    vTcl:DefineAlias "$site_3_0.but61" "addButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but62 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 4 -command callback_clear \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font15,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Clear 
    vTcl:DefineAlias "$site_3_0.but62" "clearButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but63 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 4 -command callback_lookup \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font15,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Lookup 
    vTcl:DefineAlias "$site_3_0.but63" "lookupButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but64 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 4 -command callback_quit \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font15,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Quit 
    vTcl:DefineAlias "$site_3_0.but64" "quitButton" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab65 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font13,object) -foreground {#800080} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Please enter device's information} 
    vTcl:DefineAlias "$site_3_0.lab65" "Label4" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes66 \
        -background {#8080ff} -font $::vTcl(fonts,vTcl:font18,object) \
        -foreground {#f00000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -textvariable msg -width 370 
    vTcl:DefineAlias "$site_3_0.mes66" "Message" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab37 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font17,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text {IP Address} 
    vTcl:DefineAlias "$site_3_0.lab37" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab38 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font17,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Location 
    vTcl:DefineAlias "$site_3_0.lab38" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab39 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font17,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Serial Number} 
    vTcl:DefineAlias "$site_3_0.lab39" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab41 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#8080ff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font17,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -text Model 
    vTcl:DefineAlias "$site_3_0.lab41" "Label8" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent42 \
        -background {#c0c0c0} -borderwidth 4 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable dev_location 
    vTcl:DefineAlias "$site_3_0.ent42" "Location" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent43 \
        -background {#c0c0c0} -borderwidth 4 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable dev_serial 
    vTcl:DefineAlias "$site_3_0.ent43" "Serial_num" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent44 \
        -background {#c0c0c0} -borderwidth 4 -disabledforeground {#a3a3a3} \
        -font TkFixedFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -insertbackground black -selectbackground {#c4c4c4} \
        -selectforeground black -textvariable dev_model 
    vTcl:DefineAlias "$site_3_0.ent44" "Model_num" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but45 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 4 -command callback_delete \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font15,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Delete 
    vTcl:DefineAlias "$site_3_0.but45" "deleteButton" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but46 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 4 -command callback_update \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font15,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Update 
    vTcl:DefineAlias "$site_3_0.but46" "updateButton" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent52 \
        -in $site_3_0 -x 190 -y 50 -width 50 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 240 -y 60 -width 10 -height 10 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent55 \
        -in $site_3_0 -x 250 -y 50 -width 50 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 300 -y 60 -width 10 -height 10 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent58 \
        -in $site_3_0 -x 310 -y 50 -width 50 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab59 \
        -in $site_3_0 -x 360 -y 60 -width 10 -relwidth 0 -height 10 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent60 \
        -in $site_3_0 -x 370 -y 50 -width 50 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but61 \
        -in $site_3_0 -x 20 -y 300 -width 65 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but62 \
        -in $site_3_0 -x 340 -y 300 -width 65 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but63 \
        -in $site_3_0 -x 180 -y 300 -width 65 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but64 \
        -in $site_3_0 -x 420 -y 300 -width 65 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab65 \
        -in $site_3_0 -x 90 -y 10 -width 294 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes66 \
        -in $site_3_0 -x 70 -y 240 -width 370 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab37 \
        -in $site_3_0 -x 45 -y 50 -width 100 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab38 \
        -in $site_3_0 -x 45 -y 100 -width 80 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab39 \
        -in $site_3_0 -x 45 -y 150 -width 120 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab41 \
        -in $site_3_0 -x 45 -y 200 -width 70 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent42 \
        -in $site_3_0 -x 190 -y 100 -width 232 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent43 \
        -in $site_3_0 -x 190 -y 150 -width 232 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent44 \
        -in $site_3_0 -x 190 -y 200 -width 232 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 100 -y 300 -width 65 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 260 -y 300 -width 65 -height 25 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra51 \
        -in $top -x 10 -y 10 -width 505 -relwidth 0 -height 355 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

Window show .
Window show .top50
