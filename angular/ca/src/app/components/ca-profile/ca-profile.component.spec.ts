import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CaProfileComponent } from './ca-profile.component';

describe('CaProfileComponent', () => {
  let component: CaProfileComponent;
  let fixture: ComponentFixture<CaProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CaProfileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CaProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
