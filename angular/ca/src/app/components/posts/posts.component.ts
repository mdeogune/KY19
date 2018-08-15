import { Component, OnInit } from '@angular/core';
import { CaDataService } from '../../services/ca-data.service';


import { Http, Response, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/toPromise';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import 'rxjs/add/operator/toPromise';

declare var window: any;
declare var FB: any;

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit{
  public BASE_URL: string = window.location.origin;
  public headers: Headers = new Headers({'content-type': 'application/json'})
  public posts: JSON;
  public ky_id: string;
  public email_id: string;
  public mobile_number: number;
  public paid_amt: number;
  public payment_id: string = null;
  public is_paid = null;
  public previous_reg:JSON;
   public allevents:JSON;
   public en_to_cancel;
   public referedreg
   public if_canceled: boolean = false;
  constructor(public http: Http,public caservice: CaDataService) { }

  ngOnInit(): void{


    this.caservice.getResgistration()
    .then((data) =>{
      console.log("data:");
      console.log(data.json());
      this.previous_reg = data.json();
      // for (var i in this.previous_reg){
      //   console.log(this.previous_reg[i].teamLeader)
      // }

    })
    this.caservice.getReferedregs()
    .then((data)=>{
      this.referedreg = data.json()
      console.log(this.referedreg);

    })

    this.caservice.getCaData()
    .then((data) =>{
      
      this.ky_id = data.json()['ky_id'];
      this.is_paid = data.json()['is_paid'];
      this.email_id = data.json()['email'];
      this.mobile_number = data.json()['mobile_number'];
      this.payment_id = data.json()['payment_id'];
      this.paid_amt = data.json()['paid_amt'];
    })
    .catch((err) =>{
      console.log(err);
    })


     this.caservice.getAllEvents()
    .then((data) =>{
     // console.log("data:");
     // console.log(data.json());
      this.allevents = data.json();
     
    })



   
		let url: string = `${this.BASE_URL}/api/posts/`;
	 	this.http.get(url, {headers: this.headers}).subscribe((res)=>{
			this.posts = res.json();
		});
  }

  shareIt(post_link){
    // console.log(post_link);
    window.share(post_link);
  }


   cancelRegister(event){
    this.en_to_cancel=event;
    this.if_canceled=true;
    console.log(this.if_canceled);

  }

  cancelButton(){
    this.en_to_cancel=null;
    this.if_canceled=false;
  }

yesButton(){
  var data={

    'event':this.en_to_cancel,
  }

   let url: string = `${this.BASE_URL}/api/deleteteam/`;
   const headers = new Headers(
        {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.caservice.getCookie('csrftoken')
        });

    this.http.post(url, JSON.stringify(data), {headers: headers})        
        .map(this.extractData)
        .catch(this.handleError)
        .subscribe(
        res => {
          console.log(res['status']);
          if (res['status']=="deleted"){
            //console.log("res")
            
            this.caservice.getResgistration()
                .then((data) =>{
                  console.log("data:");
                  console.log(data.json());
                  this.previous_reg = data.json();
            
      // for (var i in this.previous_reg){
      //   console.log(this.previous_reg[i].teamLeader)
      // }

    })


          }
 
        });
         this.en_to_cancel=null;
        this.if_canceled=false;
        return

}

private extractData(res: Response) {
        let body = res.json();
        return body || {};
    }

private handleError(error: any) {
    let errMsg = (error.message) ? error.message :
        error.status ? `${error.status} - ${error.statusText}` : 'Server error';
    console.error(errMsg);
    return Observable.throw(errMsg);
}
  eventName(ev){
   // console.log("da:");
    //console.log(ev);
    var i;
    var e;
    for ( i in this.allevents ){
      var subevent=this.allevents[i]
      for ( e in subevent ) {
        //console.log(subevent[e].eventId);
        if (subevent[e].eventId==ev){

          return subevent[e].eventName

        }
      }

    }

  }


}
