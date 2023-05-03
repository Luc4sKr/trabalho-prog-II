(function(){"use strict";var o={30:function(o,e,t){var n=t(9242),r=t(3396);function a(o,e,t,n,a,i){const l=(0,r.up)("HomeComponent");return(0,r.wg)(),(0,r.j4)(l)}var i=t(7139);const l=o=>((0,r.dD)("data-v-0a7f7941"),o=o(),(0,r.Cn)(),o),d={class:"wrapper"},c={class:"modal-container"},s={id:"books-list",class:"grid-container"},u={key:0},m=l((()=>(0,r._)("h2",{class:"msg-not-found"},"No registered book",-1))),_=[m],p={class:"card-modal-container"},g={key:0,class:"modal card-book-modal"},f={class:"btn-container"};function b(o,e,t,n,a,l){const m=(0,r.up)("HeaderComponent"),b=(0,r.up)("FormComponent"),v=(0,r.up)("CardComponent");return(0,r.wg)(),(0,r.iD)(r.HY,null,[(0,r.Wm)(m),(0,r._)("div",d,[(0,r._)("div",c,[(0,r._)("button",{id:"btn-modal",class:"btn",onClick:e[0]||(e[0]=(...o)=>l.toggle_form_modal&&l.toggle_form_modal(...o))},(0,i.zw)(a.btn_modal_txt),1),((0,r.wg)(),(0,r.j4)(r.lR,{to:"#modal"},[a.form_open?((0,r.wg)(),(0,r.j4)(b,{key:0})):(0,r.kq)("",!0)]))]),(0,r._)("div",s,[((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(a.books,(o=>((0,r.wg)(),(0,r.iD)("div",{class:"grid-item",key:o.id},[(0,r.Wm)(v,(0,r.dG)(o,{onClick:e=>l.open_card_modal(o.id)}),null,16,["onClick"])])))),128)),a.books.length<=0?((0,r.wg)(),(0,r.iD)("div",u,_)):(0,r.kq)("",!0)]),(0,r._)("div",p,[((0,r.wg)(),(0,r.j4)(r.lR,{to:"#modal"},[a.card_modal_open?((0,r.wg)(),(0,r.iD)("div",g,[(0,r.Wm)(v,(0,i.vs)((0,r.F4)(a.book_modal)),null,16),(0,r._)("div",f,[(0,r._)("button",{class:"btn close-btn-card-modal",onClick:e[1]||(e[1]=(...o)=>l.close_card_modal&&l.close_card_modal(...o))},"Close")])])):(0,r.kq)("",!0)]))])])],64)}const v=o=>((0,r.dD)("data-v-7e5a0349"),o=o(),(0,r.Cn)(),o),h=v((()=>(0,r._)("h1",null,"BOOK SUMMARIES",-1))),k=[h];function y(o,e,t,n,a,i){return(0,r.wg)(),(0,r.iD)("header",null,k)}var w={name:"HeaderComponent"},C=t(89);const H=(0,C.Z)(w,[["render",y],["__scopeId","data-v-7e5a0349"]]);var O=H;const D=o=>((0,r.dD)("data-v-627813dc"),o=o(),(0,r.Cn)(),o),U={class:"modal book-modal"},j={class:"form-control"},x=D((()=>(0,r._)("label",{for:"title"},"Title",-1))),q={class:"form-control"},z=D((()=>(0,r._)("label",{for:"category"},"Category",-1))),R=["value"],F={class:"form-control"},S=D((()=>(0,r._)("label",{for:"author"},"Author",-1))),V={class:"form-control"},Z={for:"grade"},I={class:"form-control"},M=D((()=>(0,r._)("label",{for:"resume"},"Resume",-1))),T={class:"form-control"},A=D((()=>(0,r._)("label",{for:"reading-time"},"Reading Time",-1))),N={class:"reading-time-input-container"},G=D((()=>(0,r._)("span",null,"Hours",-1))),K=D((()=>(0,r._)("div",{class:"buttons"},[(0,r._)("button",{id:"btn-register",class:"btn"},"Register")],-1)));function W(o,e,t,a,l,d){return(0,r.wg)(),(0,r.iD)("div",U,[(0,r._)("form",{id:"book-form",onSubmit:e[6]||(e[6]=(0,n.iM)(((...o)=>d.include_book&&d.include_book(...o)),["prevent"])),method:"post"},[(0,r._)("div",j,[x,(0,r.wy)((0,r._)("input",{id:"title-input",name:"title",type:"text","onUpdate:modelValue":e[0]||(e[0]=o=>l.book.title=o)},null,512),[[n.nr,l.book.title]])]),(0,r._)("div",q,[z,(0,r.wy)((0,r._)("select",{id:"category-input",name:"category","onUpdate:modelValue":e[1]||(e[1]=o=>l.book.category_id=o)},[((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(l.categories,(o=>((0,r.wg)(),(0,r.iD)("option",{key:o.id,value:o.id},(0,i.zw)(o.category_name),9,R)))),128))],512),[[n.bM,l.book.category_id]])]),(0,r._)("div",F,[S,(0,r.wy)((0,r._)("input",{id:"author-input",name:"author",type:"text","onUpdate:modelValue":e[2]||(e[2]=o=>l.book.author=o)},null,512),[[n.nr,l.book.author]])]),(0,r._)("div",V,[(0,r._)("label",Z,[(0,r.Uk)("Grade: "),(0,r._)("span",null,(0,i.zw)(l.book.grade),1)]),(0,r.wy)((0,r._)("input",{id:"grade-input",name:"grade",type:"range",min:"0",max:"5","onUpdate:modelValue":e[3]||(e[3]=o=>l.book.grade=o)},null,512),[[n.nr,l.book.grade]])]),(0,r._)("div",I,[M,(0,r.wy)((0,r._)("textarea",{name:"resume",id:"resume",cols:"30",rows:"10","onUpdate:modelValue":e[4]||(e[4]=o=>l.book.resume=o)},null,512),[[n.nr,l.book.resume]])]),(0,r._)("div",T,[A,(0,r._)("div",N,[(0,r.wy)((0,r._)("input",{id:"reading-time-input",name:"reading-time",type:"number","onUpdate:modelValue":e[5]||(e[5]=o=>l.book.reading_time=o)},null,512),[[n.nr,l.book.reading_time]]),G])]),K],32)])}var Y=t(4161);const E=Y.Z.create({baseURL:"http://127.0.0.1:5000/"});var P=E,B=t(4870),L={name:"FormComponent",data(){return{categories:[],book:{title:(0,B.iH)(""),author:(0,B.iH)(""),grade:(0,B.iH)(0),resume:(0,B.iH)(""),reading_time:(0,B.iH)(null),category_id:(0,B.iH)(1)}}},created(){this.fetch_categories()},methods:{fetch_categories:function(){P.get("/list/category").then((o=>{this.categories=o.data.category})).catch((o=>{console.log(o)}))},include_book:function(){P.post("/include/book",this.book).then((o=>{console.log(o)})).catch((o=>{console.log(o)}))}}};const $=(0,C.Z)(L,[["render",W],["__scopeId","data-v-627813dc"]]);var J=$;const Q=o=>((0,r.dD)("data-v-5051089e"),o=o(),(0,r.Cn)(),o),X={class:"card"},oo={class:"card-head"},eo={class:"title"},to={class:"card-body"},no={class:"infos"},ro=Q((()=>(0,r._)("strong",null,"Category: ",-1))),ao=Q((()=>(0,r._)("strong",null,"Author: ",-1))),io=Q((()=>(0,r._)("strong",null,"Grade: ",-1))),lo=Q((()=>(0,r._)("strong",null,"Reading Time: ",-1))),co={class:"resume-container"},so={class:"resume"},uo=Q((()=>(0,r._)("strong",null,"Resume: ",-1)));function mo(o,e,t,n,a,l){return(0,r.wg)(),(0,r.iD)("div",X,[(0,r._)("div",oo,[(0,r._)("h3",eo,(0,i.zw)(t.title),1)]),(0,r._)("div",to,[(0,r._)("div",no,[(0,r._)("span",null,[ro,(0,r.Uk)((0,i.zw)(t.category.category_name),1)]),(0,r._)("span",null,[ao,(0,r.Uk)((0,i.zw)(t.author),1)]),(0,r._)("span",null,[io,(0,r.Uk)(" "+(0,i.zw)(t.grade),1)]),(0,r._)("span",null,[lo,(0,r.Uk)((0,i.zw)(t.reading_time),1)])]),(0,r._)("div",co,[(0,r._)("p",so,[uo,(0,r.Uk)((0,i.zw)(t.resume),1)])])])])}var _o={name:"CardComponent",props:{id:{type:Number,required:!0},title:{type:String,required:!0},category:{type:Object,required:!0},author:{type:String,required:!0},grade:{type:Number,required:!0},reading_time:{type:Number,required:!0},resume:{type:String,required:!0}},data(){return{}},methods:{}};const po=(0,C.Z)(_o,[["render",mo],["__scopeId","data-v-5051089e"]]);var go=po,fo={name:"HomeComponent",components:{HeaderComponent:O,FormComponent:J,CardComponent:go},data(){return{form_open:!1,btn_modal_txt:"Open Form",books:[],card_modal_open:!1,book_modal:{}}},created(){this.fetch_books()},methods:{toggle_form_modal:function(){this.card_modal_open||(this.form_open=!this.form_open,this.btn_modal_txt=this.form_open?"Close Form":"Open Form")},fetch_books:function(){P.get("/list/book").then((o=>{this.books=o.data.book})).catch((o=>{console.log(o)}))},open_card_modal:async function(o){if(!this.form_open){try{const e=await P.get(`/list/book/${o}`);console.log(e.data.book),this.book_modal=e.data.book}catch(e){console.log(e)}this.card_modal_open=!0}},close_card_modal:function(){this.card_modal_open=!1}}};const bo=(0,C.Z)(fo,[["render",b],["__scopeId","data-v-0a7f7941"]]);var vo=bo,ho={name:"App",components:{HomeComponent:vo}};const ko=(0,C.Z)(ho,[["render",a]]);var yo=ko;(0,n.ri)(yo).mount("#app")}},e={};function t(n){var r=e[n];if(void 0!==r)return r.exports;var a=e[n]={exports:{}};return o[n](a,a.exports,t),a.exports}t.m=o,function(){var o=[];t.O=function(e,n,r,a){if(!n){var i=1/0;for(s=0;s<o.length;s++){n=o[s][0],r=o[s][1],a=o[s][2];for(var l=!0,d=0;d<n.length;d++)(!1&a||i>=a)&&Object.keys(t.O).every((function(o){return t.O[o](n[d])}))?n.splice(d--,1):(l=!1,a<i&&(i=a));if(l){o.splice(s--,1);var c=r();void 0!==c&&(e=c)}}return e}a=a||0;for(var s=o.length;s>0&&o[s-1][2]>a;s--)o[s]=o[s-1];o[s]=[n,r,a]}}(),function(){t.n=function(o){var e=o&&o.__esModule?function(){return o["default"]}:function(){return o};return t.d(e,{a:e}),e}}(),function(){t.d=function(o,e){for(var n in e)t.o(e,n)&&!t.o(o,n)&&Object.defineProperty(o,n,{enumerable:!0,get:e[n]})}}(),function(){t.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(o){if("object"===typeof window)return window}}()}(),function(){t.o=function(o,e){return Object.prototype.hasOwnProperty.call(o,e)}}(),function(){var o={143:0};t.O.j=function(e){return 0===o[e]};var e=function(e,n){var r,a,i=n[0],l=n[1],d=n[2],c=0;if(i.some((function(e){return 0!==o[e]}))){for(r in l)t.o(l,r)&&(t.m[r]=l[r]);if(d)var s=d(t)}for(e&&e(n);c<i.length;c++)a=i[c],t.o(o,a)&&o[a]&&o[a][0](),o[a]=0;return t.O(s)},n=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];n.forEach(e.bind(null,0)),n.push=e.bind(null,n.push.bind(n))}();var n=t.O(void 0,[998],(function(){return t(30)}));n=t.O(n)})();
//# sourceMappingURL=app.4d36256f.js.map