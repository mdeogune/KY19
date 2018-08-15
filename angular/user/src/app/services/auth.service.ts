import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class AuthService {
  private BASE_URL: string = window.location.href;
  private headers: Headers = new Headers({'content-type': 'application/json'})

  constructor(private http: Http) {
  }

  ensureAuthenticated(token): Promise <any> {
	let url: string = `${this.BASE_URL}/status`;
	let headers: Headers = new Headers({
		'Content-Type': 'application/json',
		Authorization: `Bearer ${token}`
    });
 	return this.http.get(url, {headers: headers}).toPromise();
  }
  
}
