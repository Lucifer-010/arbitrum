// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract UserData {
    struct UserInfo {
        uint256 number;
        string name;
        string aboutMe;
    }

    mapping(string => UserInfo) public userInfos;

    function addUser(uint256 _number, string memory _name, string memory _aboutMe) public {
        userInfos[_name] = UserInfo(_number, _name, _aboutMe);
    }

    function getUserInfo(string memory _name) public view returns (uint256, string memory, string memory) {
        return (userInfos[_name].number, userInfos[_name].name, userInfos[_name].aboutMe);
    }
}