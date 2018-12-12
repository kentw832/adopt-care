import { NgModule } from '@angular/core';
import { CommonModule, APP_BASE_HREF } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';


// App
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// Modules
import { CalendarModule } from './modules/calendar';
import { ModalsModule } from './modules/modals';
import { PopoverModule } from './modules/popover';
import { TimePickerModule } from './modules/time-picker';
import { ToastModule } from './modules/toast';

// Components
import {
  NavComponent,
  PatientHeaderComponent,
  PlanHeaderComponent,
  RecordResultsComponent,
  ReassignPatientsComponent,
  PlanDurationComponent,
  GoalComponent,
  AddCTTaskComponent,
  EditTaskComponent,
  AddVitalComponent,
  PreviewVitalComponent,
  CreateVitalComponent,
  AddAssessmentComponent,
  CreateAssessmentComponent,
  AddStreamComponent,
  CreateStreamComponent,
  AddPatientToPlanComponent,
  EnrollmentRequiredComponent,
  EnrollmentComponent,
  PatientEnrolledComponent,
  AddCTMemberComponent,
  PlanExpiredComponent,
  PlanLimitReachedComponent,
} from './components';

// Services
import {
  AuthService,
  CanActivateViaAuthGuard,
  AuthTokenInterceptor,
  CacheInterceptor,
  CacheService,
  HttpService,
  // MockService,
  NavbarService,
  LocalStorageService,
  SessionStorageService,
  StoreService,
  ValidationService,
} from './services';

// Routes
import {
  BillingComponent,
  DashboardComponent,
  ErrorComponent,
  FacilityComponent,
  InviteComponent,
  CreateAccountComponent,
  LoginComponent,
  ResetPasswordComponent,
  VerifyEmailComponent,
  OrganizationComponent,
  EditFacilityComponent,
  PatientComponent,
  PatientDashboardComponent,
  PatientDetailsComponent,
  PatientHistoryComponent,
  PatientMessagingComponent,
  PatientOverviewComponent,
  PatientTeamComponent,
  ActivePatientsComponent,
  InvitedPatientsComponent,
  PotentialPatientsComponent,
  InactivePatientsComponent,
  PlansComponent,
  PlanInfoComponent,
  PlanScheduleComponent,
  StyleguideComponent,
  UserComponent,
  UsersComponent,
  AddUserComponent,
  ChangeEmailComponent,
  ChangePasswordComponent,
  AddPlanComponent,
  ReminderEmailComponent,
  FinancialDetailsComponent,
  ProblemAreasComponent,
  DiagnosisComponent,
  ProcedureComponent,
  GoalCommentsComponent,
  MedicationComponent,
  PatientProfileComponent,
  PatientCommunicationComponent,
  PatientAddressComponent,
  PatientEmergencyContactComponent,
  DeleteMedicationComponent,
  DeleteDiagnosisComponent,
  EditUserDetailsComponent,
  AllModalsComponent,
} from './routes';

import { FrequencyTransformPipe } from './pipes/frequency-transform.pipe';
import { TimeTransformPipe } from './pipes/time-transform.pipe';
import { ReassignBillingPractitionerComponent } from './routes/users/modals/reassign-billing-practitioner/reassign-billing-practitioner.component';
import { DeletePlanComponent } from './routes/plans/modals/delete-plan/delete-plan.component';
import { EnrollPatientComponent } from './routes/patient/modals/enroll-patient/enroll-patient.component';
import { CarePlanConsentComponent } from './routes/patient/modals/care-plan-consent/care-plan-consent.component';
import { AddDiagnosisComponent } from './routes/patient/modals/add-diagnosis/add-diagnosis.component';
import { EditDiagnosisComponent } from './routes/patient/modals/edit-diagnosis/edit-diagnosis.component';
import { AddProcedureComponent } from './routes/patient/modals/add-procedure/add-procedure.component';
import { EditProcedureComponent } from './routes/patient/modals/edit-procedure/edit-procedure.component';
import { AddCtComponent } from './routes/patient/modals/add-ct/add-ct.component';
import { EditBillingPractitionerComponent } from './routes/patient/modals/edit-billing-practitioner/edit-billing-practitioner.component';
import { EditCcmComponent } from './routes/patient/modals/edit-ccm/edit-ccm.component';

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    CalendarModule,
    ModalsModule,
    PopoverModule,
    TimePickerModule,
    ToastModule,
    ReactiveFormsModule,
  ],
  declarations: [
    AppComponent,
    BillingComponent,
    DashboardComponent,
    ErrorComponent,
    FacilityComponent,
    EditFacilityComponent,
    InviteComponent,
    CreateAccountComponent,
    LoginComponent,
    ResetPasswordComponent,
    VerifyEmailComponent,
    NavComponent,
    PatientHeaderComponent,
    PlanHeaderComponent,
    OrganizationComponent,
    PatientComponent,
    PatientDashboardComponent,
    PatientDetailsComponent,
    PatientHistoryComponent,
    PatientMessagingComponent,
    PatientOverviewComponent,
    PatientTeamComponent,
    ActivePatientsComponent,
    InvitedPatientsComponent,
    PotentialPatientsComponent,
    InactivePatientsComponent,
    PlansComponent,
    PlanInfoComponent,
    PlanScheduleComponent,
    StyleguideComponent,
    UserComponent,
    UsersComponent,
    RecordResultsComponent,
    AddUserComponent,
    ReassignPatientsComponent,
    ChangeEmailComponent,
    ChangePasswordComponent,
    AddPlanComponent,
    PlanDurationComponent,
    GoalComponent,
    AddCTTaskComponent,
    EditTaskComponent,
    AddVitalComponent,
    PreviewVitalComponent,
    CreateVitalComponent,
    AddAssessmentComponent,
    CreateAssessmentComponent,
    AddStreamComponent,
    CreateStreamComponent,
    ReminderEmailComponent,
    AddPatientToPlanComponent,
    EnrollmentRequiredComponent,
    EnrollmentComponent,
    PatientEnrolledComponent,
    FinancialDetailsComponent,
    ProblemAreasComponent,
    DiagnosisComponent,
    ProcedureComponent,
    GoalCommentsComponent,
    MedicationComponent,
    AddCTMemberComponent,
    PlanExpiredComponent,
    PlanLimitReachedComponent,
    PatientProfileComponent,
    PatientCommunicationComponent,
    PatientAddressComponent,
    PatientEmergencyContactComponent,
    DeleteMedicationComponent,
    DeleteDiagnosisComponent,
    EditUserDetailsComponent,
    FrequencyTransformPipe,
    TimeTransformPipe,
    AllModalsComponent,
    ReassignBillingPractitionerComponent,
    DeletePlanComponent,
    EnrollPatientComponent,
    CarePlanConsentComponent,
    AddDiagnosisComponent,
    EditDiagnosisComponent,
    AddProcedureComponent,
    EditProcedureComponent,
    AddCtComponent,
    EditBillingPractitionerComponent,
    EditCcmComponent,
  ],
  providers: [
    {provide: APP_BASE_HREF, useValue: '/'},
    {provide: HTTP_INTERCEPTORS, useClass: AuthTokenInterceptor, multi: true},
    // {provide: HTTP_INTERCEPTORS, useClass: CacheInterceptor, multi: true},
    AuthService,
    CanActivateViaAuthGuard,
    CacheService,
    HttpService,
    // MockService,
    NavbarService,
    StoreService,
    LocalStorageService,
    SessionStorageService,
    ValidationService,
  ],
  bootstrap: [AppComponent],
  entryComponents: [
    EditFacilityComponent,
    RecordResultsComponent,
    AddUserComponent,
    ReassignPatientsComponent,
    ChangeEmailComponent,
    ChangePasswordComponent,
    AddPlanComponent,
    PlanDurationComponent,
    GoalComponent,
    AddCTTaskComponent,
    EditTaskComponent,
    AddVitalComponent,
    PreviewVitalComponent,
    CreateVitalComponent,
    AddAssessmentComponent,
    CreateAssessmentComponent,
    AddStreamComponent,
    CreateStreamComponent,
    ReminderEmailComponent,
    AddPatientToPlanComponent,
    EnrollmentRequiredComponent,
    EnrollmentComponent,
    PatientEnrolledComponent,
    FinancialDetailsComponent,
    ProblemAreasComponent,
    DiagnosisComponent,
    ProcedureComponent,
    GoalCommentsComponent,
    MedicationComponent,
    AddCTMemberComponent,
    PlanExpiredComponent,
    PlanLimitReachedComponent,
    PatientProfileComponent,
    PatientCommunicationComponent,
    PatientAddressComponent,
    PatientEmergencyContactComponent,
    DeleteMedicationComponent,
    DeleteDiagnosisComponent,
    EditUserDetailsComponent,
    ReassignBillingPractitionerComponent,
    DeletePlanComponent,
    EnrollPatientComponent,
    CarePlanConsentComponent,
    AddDiagnosisComponent,
    EditDiagnosisComponent,
    AddProcedureComponent,
    EditProcedureComponent,
    AddCtComponent,
    EditBillingPractitionerComponent,
    EditCcmComponent,
  ],
})
export class AppModule { }