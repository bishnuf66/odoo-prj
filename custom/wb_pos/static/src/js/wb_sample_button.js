odoo.define("wb_pos.WBSampleButton",function(require){

    "use strict";
    
    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen=require("point_of_sale.ProductScreen");
    const Registries =require("point_of_sale.Registries");
    const { useListener }=require("@web/core/utils/hooks");
    const core = require("web.core");
    var _t = core._t;



    class WBSampleButton extends PosComponent
{

    setup(){
        super.setup();
        useListener("click",this.wb_sample_button_click);
    }

    async wb_sample_button_click(){


 /*        var result = await this.rpc({
            'model':"res.lang",
            "method":"search_read",
            "args":"[[],['id','name','code']]",
        });
        console.log(result);
        result.forEach(function(value){
            console.log("record....",value);
        })

 */

        var result = await this.rpc({
            route:"/pos/rpc/example",
            params:{},
        })
        console.log (result);


       this.showPopup("ErrorPopup",{
        title:_t("Error Message"),
        body:this.env._t("this is a error message."),
        });

        
   
        /* 
    const { confirmed }=await this.showPopup("ConfirmPopup",{
        title:_t("confirm popup"),
        body:_t("are you sure want to continue?"),
        confirmText:_t("yes"),
        cancelText:_t("no")

    });

    if(confirmed){
        console.log("clicked no")}
    else {
    console.log("clicked no")
    } 
 */

/* 
    console.log("this is a click button event",confirmed);
    


    this.showPopup("OfflineErrorPopup",{
        title:_t("odoo Error"),
        body:_t("this is a test popup don't panic")
    }) */


/*     const{confirmed, payload: selectedOption}=await this.showPopup("SelectionPopup",{
        title:"this is selection popup",
        list:[{'id':0,'label':_t("yes"),'item':true},
              {'id':1,'label':_t("no"),'item':false},
              {'id':2,'label':_t("not sure"),'item':false}]
    });
    console.log(confirmed);
    console.log(selectedOption);
    */


  /*   const info =await this.env.pos.getClosePosInfo();
    this.showPopup("ClosePosPopup",{
        info:info,
        keepBehind:true
    }) */
      
    }

}
WBSampleButton.template="WBSampleButton";

ProductScreen.addControlButton({
    component:WBSampleButton,
    position:["before","OrderlineCustomerNoteButton"],
 

});

Registries.Component.add(WBSampleButton);

return WBSampleButton;

});