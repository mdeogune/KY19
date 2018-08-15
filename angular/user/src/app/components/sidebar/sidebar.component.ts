import { Component, OnInit } from '@angular/core';
import { CaDataService } from '../../services/ca-data.service';

@Component({
  selector: 'sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
	public profile_picture: string;
  public ky_id: string;

  constructor(private caservice: CaDataService) { }
  ngOnInit():void {
    this.caservice.getCaData()
    .then((data) =>{
      this.profile_picture = data.json()['profile_picture'];
      this.ky_id = data.json()['ky_id'];
    })
    .catch((err) =>{
      console.log(err);
    })
  }
}
