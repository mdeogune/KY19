import { Component, OnInit } from '@angular/core';
import { CaDataService } from '../../services/ca-data.service';

@Component({
  selector: 'navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
	constructor(public caservice: CaDataService){
	}

  public unread_notices: JSON;
  public read_notices: JSON;
  public notice_count: any;
  ngOnInit():void {
  // this.caservice.getTop5Notices()
  //   .then((data) =>{
  //     // console.log(data.json());
  //     this.unread_notices = data.json()['unread'];
  //     this.read_notices = data.json()['read'];
  //     this.notice_count = data.json()['unread'].length.toString();
  //     // console.log(typeof this.notice_count);
  //   })
  //   .catch((err) =>{
  //     console.log(err);
  //   })
  }

}
