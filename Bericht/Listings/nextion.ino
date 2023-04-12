#include<Nextion.h>

NexButton b0 = NexButton(0, 1, "b0");

char buffer[100] = {0};

NexTouch *nex_listen_list[] = //*\label{code:begin_nex_touch_list}*)
{
    &b0,
    NULL
}; //*\label{code:end_nex_touch_list}*)

void b0PopCallback(void *ptr) //*\label{code:b0PopCallback}*)
{
    uint16_t len;
    uint16_t number;
    NexButton *btn = (NexButton *)ptr; //*\label{code:cast}*)
    dbSerialPrintln("b0PopCallback");
    dbSerialPrint("ptr=");
    dbSerialPrintln((uint32_t)ptr); 
    memset(buffer, 0, sizeof(buffer));

    btn->getText(buffer, sizeof(buffer));

    number = atoi(buffer); //*\label{code:to_int_conversion}*)
    number += 1;

    memset(buffer, 0, sizeof(buffer));
    itoa(number, buffer, 10);

    btn->setText(buffer); //*\label{code:setText}*)
}

void setup(void)
{
    nexInit();

    b0.attachPop(b0PopCallback, &b0); //*\label{code:attachPop}*)

    dbSerialPrintln("setup done");
}

void loop(void)
{
    nexLoop(nex_listen_list); //*\label{code:nexLoop}*)
}