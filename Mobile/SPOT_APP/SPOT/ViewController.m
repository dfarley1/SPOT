// Copyright 2015 Google Inc. All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#import "ViewController.h"
#import "ESSEddystone.h"
#import <SafariServices/SafariServices.h>
#import <Foundation/Foundation.h>
#import "ESSBeaconScanner.h"

@interface ViewController () <ESSBeaconScannerDelegate> {
  ESSBeaconScanner *_scanner;
}
@end

// Objective-C (with modules enabled)
@import UserNotifications;

@interface SFSafariViewController () <SFSafariViewControllerDelegate>;

@end

@implementation ViewController

- (void)viewDidLoad {
  [super viewDidLoad];
  // Do any additional setup after loading the view, typically from a nib.
}

- (void)viewWillAppear:(BOOL)animated {
  [super viewWillAppear:animated];
  _scanner = [[ESSBeaconScanner alloc] init];
  _scanner.delegate = self;
  [_scanner startScanning];
}

- (void)safariViewControllerDidFinish:(SFSafariViewController *)controller {
    [self dismissViewControllerAnimated:true completion:nil];
}

- (void)viewDidDisappear:(BOOL)animated {
  [super viewDidDisappear:animated];
  [_scanner stopScanning];
  _scanner = nil;
}

// Serialize an NSData into a hexadeximal string
// Thanks to http://stackoverflow.com/questions/1305225/best-way-to-serialize-a-nsdata-into-an-hexadeximal-string
- (NSString *)hexStringFromData:(NSData *)data
{
    const unsigned char *dataBuffer = (const unsigned char *)data.bytes;
    
    if (!dataBuffer) {
        return [NSString string];
    }
    
    NSUInteger dataLength = data.length;
    NSMutableString *hexString = [NSMutableString stringWithCapacity:(dataLength * 2)];
    
    for (int i = 0; i < dataLength; ++i) {
        [hexString appendString:[NSString stringWithFormat:@"%02hhx", dataBuffer[i]]];
    }
    
    return [NSString stringWithString:hexString];
}

- (void)beaconScanner:(ESSBeaconScanner *)scanner
        didFindBeacon:(id)beaconInfo {
//  NSLog(@"I Saw an Eddystone!: %@", beaconInfo);
    ESSBeaconInfo *the_beacon = (ESSBeaconInfo*)beaconInfo;
    ESSBeaconID *beacon_id = the_beacon.beaconID;
    NSData *beacon_raw = beacon_id.beaconID;
    
    const unsigned char *dataBuffer = (const unsigned char *)beacon_raw.bytes;
    NSUInteger dataLength = beacon_raw.length;
    NSMutableString *hexString = [NSMutableString stringWithCapacity:(dataLength * 2)];
    
    for (int i = 0; i < dataLength; ++i) {
        [hexString appendString:[NSString stringWithFormat:@"%02hhx", dataBuffer[i]]];
    }
    NSLog(@"Test string: %@", hexString);
    NSString *user_name = @"test@test.test";
    NSString *password = @"test";
    NSString *url_login = @"https://alien-walker-157903.appspot.com/api/v1/auth/login/";
    NSString *urlString = [NSString stringWithFormat:@"https://alien-walker-157903.appspot.com/api/v1/auth/occupy/"];
    NSURL *url = [NSURL URLWithString:urlString];
    NSURL *urlLogin = [NSURL URLWithString:url_login];
    NSDictionary *loginJsonPacket = @{@"email": user_name,
                                      @"password": password};
    NSLog(@"%@", loginJsonPacket);
    NSDictionary *jsonPacket = @{@"email": user_name,
                                    @"beacon_id": hexString};

    NSError *error;
    
    NSData *jsonData_login = [NSJSONSerialization dataWithJSONObject:loginJsonPacket options:NSJSONWritingPrettyPrinted error:&error];
    NSData *jsonData = [NSJSONSerialization dataWithJSONObject:jsonPacket options:NSJSONWritingPrettyPrinted error:&error];
    
    NSString *saveString_login = [[NSString alloc] initWithData:jsonData_login
                                                 encoding:NSUTF8StringEncoding];
    NSString *saveString = [[NSString alloc] initWithData:jsonData
                                                 encoding:NSUTF8StringEncoding];
    
    NSString *myRequestLoginString = [NSString stringWithFormat:@"%@",saveString_login];
    NSString *myRequestString = [NSString stringWithFormat:@"%@",saveString];
    
    NSData *myRequestLoginData = [NSData dataWithBytes: myRequestLoginString.UTF8String length: myRequestLoginString.length];
    NSData *myRequestData = [NSData dataWithBytes: myRequestString.UTF8String length: myRequestString.length];
    
    NSString *postLoginLength = [NSString stringWithFormat:@"%ld", jsonData_login.length];
    NSString *postLength = [NSString stringWithFormat:@"%ld", jsonData.length];
    
    NSMutableURLRequest *request_login = [[NSMutableURLRequest alloc] init];
    request_login.URL = urlLogin;
    request_login.HTTPMethod = @"POST";
    [request_login setValue:postLoginLength forHTTPHeaderField:@"Content-Length"];
    request_login.HTTPBody = myRequestLoginData;

    NSURLSession *session_login = [NSURLSession sessionWithConfiguration:[NSURLSessionConfiguration defaultSessionConfiguration]];
    [[session_login dataTaskWithRequest:request_login completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        NSString *requestReply = [[NSString alloc] initWithData:data encoding:NSASCIIStringEncoding];
        NSLog(@"requestReply_login: %@", requestReply);
    }] resume];
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    request.URL = url;
    request.HTTPMethod = @"POST";
    [request setValue:postLength forHTTPHeaderField:@"Content-Length"];
    request.HTTPBody = myRequestData;
    
    NSString *spot_details = @"";
    NSURLSession *session = [NSURLSession sessionWithConfiguration:[NSURLSessionConfiguration defaultSessionConfiguration]];
    [[session dataTaskWithRequest:request completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        NSString *requestReply = [[NSString alloc] initWithData:data encoding:NSASCIIStringEncoding];
//        NSString *spot_details = [spot_details stringByAppendingString:requestReply];
        NSLog(@"requestReply: %@", requestReply);
    
//        NSLog(@"Spot details: %@",spot_details);
        
        // TO FIND index of SPOT
        NSRange searchResult = [requestReply rangeOfString:@", "];
        if (searchResult.location == NSNotFound) {
            NSLog(@"Search string was not found");
        } else {
            NSLog(@"'Cabrio' starts at index %lu and is %lu characters long",
                  searchResult.location,
                  searchResult.length);
        }
        NSRange range = NSMakeRange((searchResult.location+2), 1);
        NSString *spot_details = [requestReply substringWithRange:range];
        UNMutableNotificationContent* content = [[UNMutableNotificationContent alloc] init];
        content.title = [NSString localizedUserNotificationStringForKey:@"Welcome to SPOT!" arguments:nil];
        content.body = [NSString localizedUserNotificationStringForKey:[NSString stringWithFormat:@"You have arrived at: SPOT %@", spot_details] arguments:nil];
        content.sound = [UNNotificationSound defaultSound];
        
//        UNNotificationAttachment *attachment;
        NSURL *url_image =  [[NSBundle mainBundle] URLForResource:@"http://news.ucsc.edu/2008/04/images/blumenthal_faces.280.jpg" withExtension:@"jpg"];
        NSURL *fileURL = [[NSBundle mainBundle] URLForResource:@"blumenthal_faces" withExtension:@"jpg"];
        UNNotificationAttachment *attachment = [UNNotificationAttachment attachmentWithIdentifier:@"blumenthal_faces" URL:url_image options:nil error:&error];
//        attachment=[UNNotificationAttachment attachmentWithIdentifier:@"imageID"
//                                                                URL:url_image
//                                                                options:nil
//                                                                error:&error];
        content.attachments=@[attachment];
//
        // Deliver the notification in five seconds.
        UNTimeIntervalNotificationTrigger* trigger = [UNTimeIntervalNotificationTrigger
                                                      triggerWithTimeInterval:5 repeats:NO];
        UNNotificationRequest* requestnf = [UNNotificationRequest requestWithIdentifier:@"FiveSecond"
                                                                                content:content trigger:trigger];
        
        // Schedule the notification.
        UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
        [center addNotificationRequest:requestnf withCompletionHandler:^(NSError * _Nullable error) {
            if (!error) {
                NSLog(@"Local Notification succeeded");
            }
            else {
                NSLog(@"Local Notification failed");
            }
        }];
        
        
    
    }] resume];
    
    NSLog(@"POST: %@", myRequestString);
//    NSLog(@"Spot details: %@",spot_details);
//    NSRange searchResult = [spot_details rangeOfString:@"SPOT"];
//    if (searchResult.location == NSNotFound) {
//        NSLog(@"Search string was not found");
//    } else {
//        NSLog(@"'Cabrio' starts at index %lu and is %lu characters long",
//              searchResult.location,
//              searchResult.length);
//    }
    
    NSArray *cookies = [[NSHTTPCookieStorage sharedHTTPCookieStorage] cookiesForURL:request_login.URL];
    NSDictionary *headers = [NSHTTPCookie requestHeaderFieldsWithCookies:cookies];
    
    [request_login setAllHTTPHeaderFields:headers];
    

//
//    // Objective-C
//    UNMutableNotificationContent *content = [UNMutableNotificationContent new];
//    content.title = @"SPOT Verification!";
//    content.body =     content.sound = [UNNotificationSound defaultSound];
//    
//    UNMutableNotificationContent* content = [[UNMutableNotificationContent alloc] init];
//    content.title = [NSString localizedUserNotificationStringForKey:@"SPOT Verification" arguments:nil];
//    content.body = [NSString stringWithFormat:@"%@",myRequestString];
//    
//    // Configure the trigger for a 7am wakeup.
//    NSDateComponents* date = [[NSDateComponents alloc] init];
//    date.hour = 0;
//    date.minute = 0;
//    UNCalendarNotificationTrigger* trigger = [UNCalendarNotificationTrigger
//                                              triggerWithDateMatchingComponents:date repeats:NO];
//    
//    // Create the request object.
//    UNNotificationRequest* requestnotification = [UNNotificationRequest
//                                      requestWithIdentifier:@"MorningAlarm" content:content trigger:trigger];
    
    NSString *url_redirect = [NSString stringWithFormat:@"https://alien-walker-157903.appspot.com/mobile/"];
    NSURL *urlRedirect = [NSURL URLWithString:url_redirect];
    
    SFSafariViewController *svc = [[SFSafariViewController alloc] initWithURL:urlRedirect];
    svc.delegate = nil;
    [self presentViewController:svc animated:YES completion:nil];
    
}

- (void)beaconScanner:(ESSBeaconScanner *)scanner didUpdateBeacon:(id)beaconInfo {
//  NSLog(@"I Updated an Eddystone!: %@", beaconInfo);
}

- (void)beaconScanner:(ESSBeaconScanner *)scanner didFindURL:(NSURL *)url {
//  NSLog(@"I Saw a URL!: %@", url);
}

@end
