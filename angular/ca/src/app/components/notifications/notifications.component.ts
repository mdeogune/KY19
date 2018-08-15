import { Component, OnInit } from '@angular/core';
import { Headers, Http } from '@angular/http';

@Component({
  selector: 'app-notifications',
  templateUrl: './notifications.component.html',
  styleUrls: ['./notifications.component.css']
})
export class NotificationsComponent implements OnInit {
  public BASE_URL: string = window.location.origin;
  public headers: Headers = new Headers({'content-type': 'application/json'})
  public notifications: JSON;
  constructor(private http: Http) { }

  ngOnInit(): void{
		let url: string = `${this.BASE_URL}/api/all-notifications/`;
	 	this.http.get(url, {headers: this.headers}).subscribe((res)=>{
			this.notifications = res.json();
		});
  }


}
